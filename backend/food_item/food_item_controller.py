from typing import List
from fastapi import APIRouter, status, HTTPException
from common.fields.object_id import ObjectId
from food_item.food_item_dtos import CreateFoodItemResponse, CreateFoodItemData, UpdateFoodItemData
from food_item.food_item_model import FoodItem
from food_item.food_item_service import FoodItemService


class FoodItemController:
    def __init__(self, service: FoodItemService):
        self.router = APIRouter(prefix="/api/food-items")
        self.service = service

        # Define routes
        self.router.add_api_route("/", self.create_food_item, methods=["POST"], response_model=CreateFoodItemResponse,
                                  status_code=status.HTTP_201_CREATED)
        self.router.add_api_route("/{id}", self.get_food_item, methods=["GET"], response_model=FoodItem)
        self.router.add_api_route("/", self.get_all_food_items, methods=["GET"], response_model=List[FoodItem])
        self.router.add_api_route("/{id}", self.update_food_item, methods=["PUT"], response_model=FoodItem)
        self.router.add_api_route("/{id}", self.delete_food_item, methods=["DELETE"],
                                  status_code=status.HTTP_204_NO_CONTENT)

    async def create_food_item(self, food_item: CreateFoodItemData):
        food_item_id = self.service.create_food_item(food_item)
        return {"id": food_item_id}

    async def get_food_item(self, id: ObjectId):
        food_item = self.service.get_food_item_by_id(id)
        if food_item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food item not found")
        return food_item

    async def get_all_food_items(self):
        return self.service.get_all_food_items()

    async def update_food_item(self, id: ObjectId, food_item: UpdateFoodItemData):
        updated_food_item = self.service.update_food_item(id, food_item)
        if updated_food_item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food item not found")
        return updated_food_item

    async def delete_food_item(self, id: ObjectId):
        success = self.service.delete_food_item(id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food item not found")
        return None
