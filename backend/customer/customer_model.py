from pydantic import BaseModel, Field

from common.fields.object_id import ObjectId


class Customer(BaseModel):
    id: ObjectId = Field(alias="_id")
    name: str
    email: str
    hashedPassword: str
    phone: str
