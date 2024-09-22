from typing import Optional, List
from common.fields.object_id import ObjectId
from food_item.food_item_dtos import CreateFoodItemData, UpdateFoodItemData
from food_item.food_item_model import FoodItem
from food_item.food_item_repository import FoodItemRepository


class FoodItemService:
    def __init__(self, food_item_repository: FoodItemRepository):
        self.food_item_repository = food_item_repository

    def create_food_item(self, food_item_data: CreateFoodItemData) -> ObjectId:
        return self.food_item_repository.create_food_item(food_item_data)

    def get_food_item_by_id(self, id: ObjectId) -> Optional[FoodItem]:
        return self.food_item_repository.get_food_item_by_id(id)

    def get_all_food_items(self) -> List[FoodItem]:
        return self.food_item_repository.get_all_food_items()

    def update_food_item(self, id: ObjectId, food_item_data: UpdateFoodItemData) -> Optional[FoodItem]:
        return self.food_item_repository.update_food_item(id, food_item_data)

    def delete_food_item(self, id: ObjectId) -> bool:
        return self.food_item_repository.delete_food_item(id)
