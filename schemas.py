from pydantic import BaseModel, EmailStr


class ContactFormInput(BaseModel):
    name: str
    email: EmailStr
    message: str


class ContactFormResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    message: str