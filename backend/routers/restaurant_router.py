from fastapi import APIRouter, status

from config.database import db
from models.restaurant import Restaurant

router = APIRouter(prefix="/api/restaurants")
collection_name = db["restaurants"]

@router.get("/")
async def get_restaurants():
    restaurants_cursor = collection_name.find()
    restaurants = [Restaurant(**x) for x in restaurants_cursor]
    return restaurants


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_restaurant(restaurant: Restaurant):
    collection_name.insert_one(dict(restaurant))
