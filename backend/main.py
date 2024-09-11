from fastapi import FastAPI

from routers.restaurant_router import router as restaurant_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, there world!"}

app.include_router(restaurant_router)