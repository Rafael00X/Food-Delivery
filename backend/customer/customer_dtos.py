from typing import Optional

from pydantic import BaseModel

from common.fields.object_id import ObjectId


class CreateCustomerData(BaseModel):
    name: str
    email: str
    hashedPassword: str
    phone: str

class CreateCustomerResponse(BaseModel):
    id: ObjectId

class UpdateCustomerData(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    hashedPassword: Optional[str] = None
    phone: Optional[str] = None
