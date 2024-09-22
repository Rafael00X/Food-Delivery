from typing import Optional, List
from pymongo.collection import Collection
from pymongo.database import Database
from common.fields.object_id import ObjectId
from food_item.food_item_model import FoodItem
from food_item.food_item_dtos import CreateFoodItemData, UpdateFoodItemData


class FoodItemRepository:
    def __init__(self, db: Database):
        self.collection: Collection = db.get_collection('food_items')

    def create_food_item(self, food_item: CreateFoodItemData) -> ObjectId:
        result = self.collection.insert_one(food_item.model_dump(by_alias=True, exclude_none=True))
        return ObjectId(result.inserted_id)

    def get_food_item_by_id(self, id: ObjectId) -> Optional[FoodItem]:
        result = self.collection.find_one({"_id": id})
        if result:
            return FoodItem(**result)
        return None

    def get_all_food_items(self) -> List[FoodItem]:
        result = self.collection.find()
        food_items = [FoodItem(**x) for x in result]
        return food_items

    def update_food_item(self, id: ObjectId, food_item: UpdateFoodItemData) -> Optional[FoodItem]:
        result = self.collection.update_one(
            {"_id": id},
            {"$set": food_item.model_dump(by_alias=True, exclude_none=True)}
        )
        if result.modified_count:
            return self.get_food_item_by_id(id)
        return None

    def delete_food_item(self, id: ObjectId) -> bool:
        result = self.collection.delete_one({"_id": id})
        return result.deleted_count == 1
