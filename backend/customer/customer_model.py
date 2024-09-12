from typing import Optional

from pydantic import BaseModel, Field

from common.fields.object_id import ObjectId


class Customer(BaseModel):
    id: ObjectId = Field(alias="_id")
    name: str
    email: str
    hashedPassword: str
    phone: str

class CustomerCreate(BaseModel):
    name: str
    email: str
    hashedPassword: str
    phone: str

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    hashedPassword: Optional[str] = None
    phone: Optional[str] = None