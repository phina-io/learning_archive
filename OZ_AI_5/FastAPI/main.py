from fastapi import FastAPI, Path, Query, HTTPException, Body
from schema import UserSignUpRequest, UserUpdateRequest, UserResponse
from connection import SessionFactory
from models import User

app = FastAPI()

#---------------------------------------------------------
# 1) 행위(Action) -> HTTP Method (GET, POST, PUT/PATCH, DELETE)
# 2) 대상(Resource) -> URL(= Uniform Resource Locator)
# HTTP Method + URL(Resource)
#---------------------------------------------------------

# 임시 데이터베이스
users = [
    {"id": 1, "name": "alex", "password": "1234"},
    {"id": 2, "name": "bob", "password": "5678"},
    {"id": 3, "name": "chris", "password": "9012"}
]

@app.get(
    "/users",
    summary="전체 사용자 조회 API",
    response_model=list[UserResponse],
    status_code=200   # 응답이 성공한 경우, 사용할 상태코드 값 지정
)
def get_users_handler():
    return users

#---------------------------------------------------------
# GET
#---------------------------------------------------------

@app.get("/hello")       # 함수 호출 조건을 데코레이터로 추가
def hello():
    return {"msg": "hello"}


# 고정API가 동적 API보다 앞에 있어야 함
# Query Parameter
# GET /users/search?name=alex
@app.get(
    "/users/search", 
    summary="회원 검색 API",
    response_model=list[UserResponse],
    status_code=200
)
def search_user_handler(
    name: str | None = Query(None)
):
    result = []
    if name is None:
        return result
    
    for user in users:
        if name in user["name"]:
            result.append(user)
    return result


# 패스 파라미터(Path Parameter)를 활용
# 변수 부분에 { }를 사용
# 가변적인 값 user_id = 10을 변수로 받기
@app.get(
    "/users/{user_id}", 
    summary="회원 조회 API",
    response_model=UserResponse,
    status_code=200
)
def get_user_handler(
    user_id: int = Path(..., ge=1)
):
    for user in users:
        if user_id == user["id"]:
            return user
        
    # user_id에 해당하는 user가 없는 경우
    raise HTTPException(
        status_code = 404,
        detail = "존재하지 않는 사용자 ID입니다."
    )


# ------------------------------------------------------------
# POST
#---------------------------------------------------------

@app.post(
    "/users", 
    summary="회원 가입 API", 
    response_model=UserResponse,
    status_code=201
)

def user_sign_up_handler(
    # 클라이언트가 보낸 데이터를 검사하고, 유효성 검사가 끝난 데이터
    body: UserSignUpRequest 
):
    new_user = User(name=body.name, password=body.password)
    session = SessionFactory()
    session.add(new_user)
    session.commit()
    
    return new_user


# patch 수정하기
@app.patch(
    "/users/{user_id}",
    summary="회원 정보 수정 API",
    response_model=UserResponse,
    status_code=200
)
def update_user_handler(
    user_id: int = Path(..., ge=1),
    body: UserUpdateRequest = Body(...)
):
    for user in users:
        if user_id == user["id"]: 
            # 요청 본문의 name 필드가 None이 아닌 경우 = 클라이언트가 데이터를 보낸 경우
            if body.name is not None:
                user["name"] == body.name
            
            # body.password가 없는 경우
            if body.password is not None:
                user["password"] == body.password
            return user
        
    raise HTTPException(
    status_code = 404,
    detail = "존재하지 않는 사용자 ID입니다."
    )
    

# 회원 삭제
@app.delete(
    "/users/{user_id}",
    summary="회원 삭제 API",
    response_model=None,
    status_code=204   # NO CONTENT
)
def delete_user_handler(
    user_id: int = Path(..., ge=1)
):
    for user in users:
        if user_id == user["id"]:
            users.remove(user)
            return
    
        raise HTTPException(
    status_code = 404,
    detail = "존재하지 않는 사용자 ID입니다."
    )