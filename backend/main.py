from fastapi import FastAPI

from common.config.database import create_db_connection
from customer.customer_controller import CustomerController
from customer.customer_repository import CustomerRepository
from customer.customer_service import CustomerService
from food_item.food_item_controller import FoodItemController
from food_item.food_item_repository import FoodItemRepository
from food_item.food_item_service import FoodItemService
from restaurant.restaurant_controller import RestaurantController
from restaurant.restaurant_repository import RestaurantRepository
from restaurant.restaurant_service import RestaurantService

app = FastAPI()
db = create_db_connection("mongodb://127.0.0.1:27017/", "Food-Delivery")


@app.get("/")
async def root():
    return {"message": "Hello World!"}


# Customer Module
customer_repository = CustomerRepository(db)
customer_service = CustomerService(customer_repository)
customer_controller = CustomerController(customer_service)
app.include_router(customer_controller.router)

# Restaurant Module
restaurant_repository = RestaurantRepository(db)
restaurant_service = RestaurantService(restaurant_repository)
restaurant_controller = RestaurantController(restaurant_service)
app.include_router(restaurant_controller.router)

# Food Item Module
food_item_repository = FoodItemRepository(db)
food_item_service = FoodItemService(food_item_repository)
food_item_controller = FoodItemController(food_item_service)
app.include_router(food_item_controller.router)
