import anyio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Path, Query, HTTPException, Body, Depends, Request
from fastapi.responses import StreamingResponse

from sqlalchemy import select
from llama_cpp import Llama

from schema import UserSignUpRequest, UserUpdateRequest, UserResponse, UserInputRequest

from connection_async import AsyncSessionFactory, get_async_session
from models import User


# Lifespan
# 서버 시작 -> 동작 -> 서버 종료
@asynccontextmanager
async def lifespan(app):
    # 서버 시작 전에 실행할 코드
    limiter = anyio.to_thread.current_default_thread_limiter()
    limiter.total_tokens = 100
    
    app.state.llm = Llama(
    model_path="./models/Llama-3.2-1B-Instruct-Q4_K_M.gguf",
    n_ctx=4096,
    n_threads=2,
    verbose=False,
    chat_format="llama-3"
)
    yield
    # 서버 종료 전에 실행할 코드
    
    
app = FastAPI(lifespan=lifespan)

#---------------------------------------------------------
# 1) 행위(Action) -> HTTP Method (GET, POST, PUT/PATCH, DELETE)
# 2) 대상(Resource) -> URL(= Uniform Resource Locator)
# HTTP Method + URL(Resource)
#---------------------------------------------------------

#---------------------------------------------------------
# GET
#---------------------------------------------------------

@app.get(
    "/users",
    summary="전체 사용자 조회 API",
    response_model=list[UserResponse],
    status_code=200   # 응답이 성공한 경우, 사용할 상태코드 값 지정
)

async def get_users_handler(
    # fastapi에게 함수 호출의 역할 부여
    session = Depends(get_async_session)
):
    stmt = select(User)    # SQL문: SELECT * FROM user 
    
    result = await session.execute(stmt)
    users: list[User] = result.scalars().all()
    return users


# 고정API가 동적 API보다 앞에 있어야 함
# Query Parameter
# GET /users/search?name=alex
@app.get(
    "/users/search", 
    summary="회원 검색 API",
    response_model=list[UserResponse],
    status_code=200
)

async def search_user_handler(
    # GET /users/search?name=alex
    name: str | None = Query(None),
    session = Depends(get_async_session)
):
    if name is None:
        return []
    
    # 검색어(name)를 name 컬럼에 포함하는 사용자 조회
    stmt = select(User).where(User.name.contains(name))
    
    result = await session.execute(stmt)
    users: list[User] = result.scalars().all()
    return users


# 패스 파라미터(Path Parameter)를 활용
# 변수 부분에 { }를 사용
# 가변적인 값 user_id = 10을 변수로 받기
@app.get(
    "/users/{user_id}", 
    summary="회원 조회 API",
    response_model=UserResponse,
    status_code=200
)

async def get_user_handler(
    user_id: int = Path(..., ge=1),
    session = Depends(get_async_session)
):
    # Python 구현한 SQL 쿼리문
    stmt = select(User).where(User.id == user_id)
    
    result = await session.execute(stmt)
    user: User | None = result.scalar()
        
    # user_id에 해당하는 user가 없는 경우
    if user is None:
        raise HTTPException(
            status_code = 404,
            detail = "존재하지 않는 사용자 ID입니다."
        )
    return user


# ------------------------------------------------------------
# POST
#---------------------------------------------------------

@app.post(
    "/users", 
    summary="회원 가입 API", 
    response_model=UserResponse,
    status_code=201
)

async def user_sign_up_handler(
    # 클라이언트가 보낸 데이터를 검사하고, 유효성 검사가 끝난 데이터
    body: UserSignUpRequest,
    session = Depends(get_async_session)
):
    new_user = User(name=body.name, password=body.password)

    session.add(new_user)
    await session.commit()
    return new_user


# 정보 수정 하기
@app.patch(
    "/users/{user_id}",
    summary="회원 정보 수정 API",
    response_model=UserResponse,
    status_code=200
)

async def update_user_handler(
    user_id: int = Path(..., ge=1),
    body: UserUpdateRequest = Body(...),
    session = Depends(get_async_session)
):
    stmt =select(User).where(User.id == user_id)
    
    result = await session.execute(stmt)
    user = result.scalar()
    if user is None : 
        raise HTTPException(
            status_code=404,
            detail= "존재하지 않는 사용자 ID 입니다."
        )
    
    if body.name:
    # if body.name is not None:
        user.name = body.name
        
    if body.password:
    # if body.password is not None:
        user.password = body.password
        
    await session.commit()
    return user


# 회원 삭제
@app.delete(
    "/users/{user_id}",
    summary="회원 삭제 API",
    response_model=None,
    status_code=204   # NO CONTENT
)

async def delete_user_handler(
    user_id: int = Path(..., ge=1),
    session = Depends(get_async_session)
):
    stmt =select(User).where(User.id == user_id)
    
    result = await session.execute(stmt)
    user = result.scalar()
    if user is None : 
        raise HTTPException(
            status_code=404,
            detail= "존재하지 않는 사용자 ID 입니다."
        )
        
    await session.delete(user) #삭제 마킹
    await session.commit()
    
def get_llm(request: Request):
    return request.app.state.llm
    
# 챗봇
@app.post("/chats")
def generate_answer_handler(
    body: UserInputRequest,  # 요청 본문
    llm = Depends(get_llm),
):
    SYSTEM_PROMPT = (
        "You are a concise assistant. "
        "Always reply in the same language as the user's input. "
        "Do not change the language. "
        "Do not mix languages."
    )
    
    # 토큰이 생성될 때마다, 토큰을 반환하는 함수
    def token_generator():
        response = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": body.user_input},
            ],
            max_tokens=256,
            temperature=0.7,     # 답변의 자유도/변동성
            stream=True
        )
        for chunk in response:
            token = chunk["choices"][0]["delta"].get("content")
            if token:
                yield token
    
    return StreamingResponse(
        # 제너레이터 객체 -> 여러 개의 데이터를 만들어주는 객체
        token_generator(),
        media_type="text/event-stream"
    )