from typing import Optional

from pydantic import BaseModel, Field

from models.object_id import PyObjectId


class Restaurant(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    description: str
    open: bool