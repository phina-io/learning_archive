from fastapi import FastAPI, Path, Query
from sqlalchemy import select

from models import User

app = FastAPI()

# [실습]
# 클라이언트가 /hi 로 GET 요청했을 때, "hi"가 출력되게
@app.get("/hi")
def hi():
    return "hi"


# [실습]
# 클라이언트가 /hi/world 로 GET 요청했을 때, "hi, world"가 출력되게
@app.get("/hi/world")
def hi():
    return "hi, world"


# [실습]
# GET /users/10 요청했을 때, {"id": 10, "name": "david"} 응답
@app.get("/users/10")
def get_user():
    return {"id": 10, "name": "david"}


# [실습] 
# 1) q: str, limit: int 두 개의 쿼리 파라미터를 받기
# 2) q: 필수, limit: 필수 아님(기본: 10)
@app.get("/items/search}")
def search_item_handler(
    q: str = Query(...), 
    limit: int = Query(10)
):
    return {"q": q, "limit": limit}


# [실습] 
# 1) item_name을 str 타입으로 고정
# 2) item_name의 최대 글자수(max_length)을 6글자로 고정
@app.get("items/{item_name}")
def get_item_handler(
    item_name: str = Path(..., max_length=6)):
    return {"item_name": item_name}


# [SQL -> Python]
# SELECT name FROM user;
select(User.name)

# SELECT name, password FROM user;
select(User.name, User.password)

# SELECT * FROM user WHERE id = 1;
select(User).where(User.id == 1)

# SELECT password FROM user WHERE name != "alex";
select(User.password).where(User.name !="alex")
