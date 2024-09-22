from typing import Optional, List

from pydantic import BaseModel

from common.fields.object_id import ObjectId
from common.fields.address import Address


class CreateRestaurantData(BaseModel):
    name: str
    address: Address
    open_time: str
    close_time: str
    menu: List[ObjectId]


class CreateRestaurantResponse(BaseModel):
    id: ObjectId


class UpdateRestaurantData(BaseModel):
    name: Optional[str] = None
    address: Optional[Address] = None
    open_time: Optional[str] = None
    close_time: Optional[str] = None
    menu: Optional[List[ObjectId]] = None
