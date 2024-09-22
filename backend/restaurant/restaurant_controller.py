from typing import List

from fastapi import APIRouter, status, HTTPException

from common.fields.object_id import ObjectId
from restaurant.restaurant_dtos import CreateRestaurantResponse, CreateRestaurantData, UpdateRestaurantData
from restaurant.restaurant_model import Restaurant
from restaurant.restaurant_service import RestaurantService


class RestaurantController:
    def __init__(self, service: RestaurantService):
        self.router = APIRouter(prefix="/api/restaurants")
        self.service = service

        # Define routes
        self.router.add_api_route("/", self.create_restaurant, methods=["POST"], response_model=CreateRestaurantResponse, status_code=status.HTTP_201_CREATED)
        self.router.add_api_route("/{id}", self.get_restaurant, methods=["GET"], response_model=Restaurant)
        self.router.add_api_route("/", self.get_all_restaurants, methods=["GET"], response_model=List[Restaurant])
        self.router.add_api_route("/{id}", self.update_restaurant, methods=["PUT"], response_model=Restaurant)
        self.router.add_api_route("/{id}", self.delete_restaurant, methods=["DELETE"], status_code=status.HTTP_204_NO_CONTENT)

    async def create_restaurant(self, restaurant: CreateRestaurantData):
        restaurant_id = self.service.create_restaurant(restaurant)
        return {"id": restaurant_id}

    async def get_restaurant(self, id: ObjectId):
        restaurant = self.service.get_restaurant_by_id(id)
        if restaurant is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
        return restaurant

    async def get_all_restaurants(self):
        return self.service.get_all_restaurants()

    async def update_restaurant(self, id: ObjectId, restaurant: UpdateRestaurantData):
        updated_restaurant = self.service.update_restaurant(id, restaurant)
        if updated_restaurant is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
        return updated_restaurant

    async def delete_restaurant(self, id: ObjectId):
        success = self.service.delete_restaurant(id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
        return None
