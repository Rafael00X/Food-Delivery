from typing import Optional, List

from pymongo.collection import Collection
from pymongo.database import Database

from common.fields.object_id import ObjectId
from restaurant.restaurant_model import Restaurant
from restaurant.restaurant_dtos import CreateRestaurantData, UpdateRestaurantData


class RestaurantRepository:
    def __init__(self, db: Database):
        self.collection: Collection = db.get_collection('restaurants')

    def create_restaurant(self, restaurant: CreateRestaurantData) -> ObjectId:
        result = self.collection.insert_one(restaurant.model_dump(by_alias=True, exclude_none=True))
        return ObjectId(result.inserted_id)

    def get_restaurant_by_id(self, id: ObjectId) -> Optional[Restaurant]:
        result = self.collection.find_one({"_id": id})
        if result:
            return Restaurant(**result)
        return None

    def get_all_restaurants(self) -> List[Restaurant]:
        result = self.collection.find()
        restaurants = [Restaurant(**x) for x in result]
        return restaurants

    def update_restaurant(self, id: ObjectId, restaurant: UpdateRestaurantData) -> Optional[Restaurant]:
        result = self.collection.update_one(
            {"_id": id},
            {"$set": restaurant.model_dump(by_alias=True, exclude_none=True)}
        )
        if result.modified_count:
            return self.get_restaurant_by_id(id)
        return None

    def delete_restaurant(self, id: ObjectId) -> bool:
        result = self.collection.delete_one({"_id": id})
        return result.deleted_count == 1
