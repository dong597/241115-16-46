from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str  # 이미지의 경로
    description: str  # 이벤트에 대한 설명(주석)
    tags: List[str] 
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "fastapi study",
                "image": "http://www.test.com/1.jpg",
                "description": "간단한 설명을 추가하세요",
                "tags": ["python", "fastapi", "study"],
                "location": "google meet"
            }
        }