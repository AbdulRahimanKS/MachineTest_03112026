from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from database import engine, Base, get_db
from schemas import ContactFormInput, ContactFormResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import ContactForm


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.post("/create_contact", response_model=ContactFormResponse)
async def create_contact(
    contact_form: ContactFormInput,
    db: AsyncSession = Depends(get_db)
):
    new_contact = ContactForm(**contact_form.model_dump())
    db.add(new_contact)
    await db.commit()
    await db.refresh(new_contact)

    return new_contact


@app.get("/list_contactform", response_model=list[ContactFormResponse])
async def list_contactforms(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ContactForm))
    contact_forms = result.scalars().all()

    return contact_forms
