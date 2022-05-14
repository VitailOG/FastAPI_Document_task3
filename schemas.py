from datetime import date

from pydantic import BaseModel


class DocumentResponseSchema(BaseModel):
    id: int
    text: str
    created_date: date
    rubrics: list[str] | None

    class Config:
        orm_mode = True
