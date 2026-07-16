import re
from pydantic import BaseModel, Field, field_validator

# 회원가입 요청에 사용되는 데이터 형식
class UserSignUpRequest(BaseModel):
    name: str = Field(..., min_length=2)
    password: str = Field(..., min_length=4, max_length=10)
    
    # 비밀번호에 대, 소문자 포함 여부 검사 코드
    # @field_validator
    # @classmethod
    # def valiate_password(cls, value):
    #     if not re.search(r"[A-Z]", value):
    #         raise ValueError("대문자가 최소 1개 이상 포함되어야 합니다.")
        
    # def valiate_password(cls, value):
    #     if not re.search(r"[a-z]", value):
    #         raise ValueError("소문자가 최소 1개 이상 포함되어야 합니다.")
        
    #     return value


# 회원 정보 수정 요청에 사용되는 데이터 형식
class UserUpdateRequest(BaseModel):
    name: str | None = Field(None, min_length=2)
    password: str | None = Field(None, min_length=4, max_length=10)
    
    
# 사용자 데이터를 응답할 때 사용하는 데이터 형식
class UserResponse(BaseModel):
    id: int
    name: str
    
    
