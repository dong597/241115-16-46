from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

# event 객체 설정 회원가입,로그인과 구별하기 위해 tags 사용
event_router = APIRouter(
    tags=["Events"]
)

events = []

# 전체 이벤트 출력하기
@event_router.get("/", response_model=List[Event])
async def all_events() -> List[Event]:
    return events

# 특정 이벤트 출력하기
@event_router.get("/{id}", response_model=Event)
async def single_events(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="해당 id는 존재하지 않습니다"
    )

# 이벤트 생성 구문
@event_router.post("/new")
async def create_events(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message" : "새로운 이벤트가 생성되었습니다"
    }

# 단일 이벤트 삭제 
@event_router.delete("/{id}")
async def delete_events(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return{
                "message" : "해당 이벤트가 삭제 되었습니다"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="입력된 id는 존재하지 않습니다"
    )

# 전체 이벤트 삭제 
@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return{
        "message" : "모든 이벤트가 삭제 되었습니다"
        }