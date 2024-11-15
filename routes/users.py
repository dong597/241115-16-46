from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIN

user_router = APIRouter(
    tags=["User"]
)

users = {}

# 유저 등록 구문
@user_router.post("/signup")
async def sign_new_user(data:User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="사용자가 이미 존재합니다"
        )
    users[data.email] = data
    return {
        "message" : "가입되었습니다"
    }

# 유저 확인 구문

@user_router.post("/signin")
async def sign_user_in(user:UserSignIN) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 사용자입니다"
        )
    
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="잘못된 패스워드입니다"
        )

    return {
        "message" : "로그인 완료 되었습니다"
    }