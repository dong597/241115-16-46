from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

# 회원가입
class User(BaseModel):
    email: EmailStr
    password: str
    evnets: Optional[List[Event]] = None

    class Config:
        json_schema_extra = {
            "example": {
                 "email": "fastapi@test.pri",
                 "password": "test123pwd",
                 "events": []
            }
        }

# 사용자 로그인 모델
class UserSignIN(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                 "email": "fastapi@test.pri",
                 "password": "test123pwd",
                 "events": []
            }
        }