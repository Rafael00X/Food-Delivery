# from fastapi import APIRouter, status, HTTPException
# from pydantic import ValidationError
#
# from common.config.database import db
# from common.fields.object_id import ObjectId
#
# from restaurant.restaurant_model import Restaurant
#
# restaurant_router = APIRouter(prefix="/api/restaurants")
# collection_name = db["restaurants"]
#
# @restaurant_router.get("/")
# async def get_restaurants():
#     restaurants_cursor = collection_name.find()
#     restaurants = [Restaurant(**x) for x in restaurants_cursor]
#     return restaurants
#
#
# @restaurant_router.post("/", status_code=status.HTTP_201_CREATED)
# async def post_restaurant(restaurant: Restaurant):
#     restaurant_dict = dict(restaurant)
#     result = collection_name.insert_one(restaurant_dict)
#     id = ObjectId(result.inserted_id)
#     return {"id": id}
#
#
# @restaurant_router.delete("/{id}", status_code=status.HTTP_200_OK)
# async def delete_restaurant(id: ObjectId):
#     try:
#         result = collection_name.delete_one({"_id": id})
#     except ValidationError as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
#
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
#
#     return {"message": "Restaurant deleted successfully"}