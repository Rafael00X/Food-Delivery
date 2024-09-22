from typing import List

from pydantic import BaseModel, Field

from common.fields.address import Address
from common.fields.object_id import ObjectId


class Restaurant(BaseModel):
    id: ObjectId = Field(alias="_id")
    name: str
    address: Address
    open_time: str
    close_time: str
    menu: List[ObjectId]