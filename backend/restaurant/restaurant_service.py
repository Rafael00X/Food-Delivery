from typing import Optional, List

from common.fields.object_id import ObjectId
from restaurant.restaurant_dtos import CreateRestaurantData, UpdateRestaurantData
from restaurant.restaurant_model import Restaurant
from restaurant.restaurant_repository import RestaurantRepository


class RestaurantService:
    def __init__(self, restaurant_repository: RestaurantRepository):
        self.restaurant_repository = restaurant_repository

    def create_restaurant(self, restaurant_data: CreateRestaurantData) -> ObjectId:
        return self.restaurant_repository.create_restaurant(restaurant_data)

    def get_restaurant_by_id(self, id: ObjectId) -> Optional[Restaurant]:
        return self.restaurant_repository.get_restaurant_by_id(id)

    def get_all_restaurants(self) -> List[Restaurant]:
        return self.restaurant_repository.get_all_restaurants()

    def update_restaurant(self, id: ObjectId, restaurant_data: UpdateRestaurantData) -> Optional[Restaurant]:
        return self.restaurant_repository.update_restaurant(id, restaurant_data)

    def delete_restaurant(self, id: ObjectId) -> bool:
        return self.restaurant_repository.delete_restaurant(id)
