from fastapi import FastAPI

from common.config.database import create_db_connection
from customer.customer_controller import CustomerController
from customer.customer_repository import CustomerRepository
from customer.customer_service import CustomerService

app = FastAPI()
db = create_db_connection()

@app.get("/")
async def root():
    return {"message": "Hello, there world!"}

# Customer Module
customer_repository = CustomerRepository(db)
customer_service = CustomerService(customer_repository)
customer_controller = CustomerController(customer_service)
app.include_router(customer_controller.router)