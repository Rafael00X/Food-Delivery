from typing import Optional, List
from pydantic import BaseModel
from common.fields.object_id import ObjectId


class CreateFoodItemData(BaseModel):
    name: str
    description: str
    tags: List[str]
    rating: str


class CreateFoodItemResponse(BaseModel):
    id: ObjectId


class UpdateFoodItemData(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    rating: Optional[str] = None
