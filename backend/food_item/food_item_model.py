from typing import List

from pydantic import BaseModel, Field

from common.fields.object_id import ObjectId


class FoodItem(BaseModel):
    id: ObjectId = Field(alias="_id")
    name: str
    description: str
    tags: List[str]
    rating: str
