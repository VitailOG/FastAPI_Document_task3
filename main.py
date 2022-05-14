from fastapi import FastAPI, Depends

from sqlalchemy import select, delete, desc

from db import get_session, Document
from schemas import DocumentResponseSchema

app = FastAPI()


@app.get('/', response_model=list[DocumentResponseSchema])
async def documents(
        search: str | None = None,
        session: get_session = Depends(get_session),
):
    async with session as s:
        l = select(Document).order_by(desc(Document.created_date)).limit(10)
        if search is not None:
            l = l.where(Document.text.ilike(f'%{search}%'))
        res = await s.execute(l)
        return res.scalars().all()


@app.delete('/{id}')
async def delete_document(
        id: int,
        session: get_session = Depends(get_session),
):
    async with session as s:
        async with s.begin():
            print(dir(s))
            d = delete(Document).where(Document.id == id)
            await s.execute(d)
