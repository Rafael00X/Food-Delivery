# from typing import Optional
#
# from pydantic import BaseModel, Field
#
# from common.fields.object_id import ObjectId
#
#
# class Restaurant(BaseModel):
#     id: Optional[ObjectId] = Field(alias="_id", default=None)
#     name: str
#     description: str
#     open: bool