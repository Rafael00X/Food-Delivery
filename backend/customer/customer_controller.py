from typing import List

from fastapi import APIRouter, status, HTTPException

from common.fields.object_id import ObjectId
from customer.customer_model import Customer, CustomerUpdate, CustomerCreate
from customer.customer_service import CustomerService


class CustomerController:
    def __init__(self, service: CustomerService):
        self.router = APIRouter(prefix="/api/customers")
        self.service = service

        # Define routes
        self.router.add_api_route("/", self.create_customer, methods=["POST"])
        self.router.add_api_route("/{id}", self.get_customer, methods=["GET"], response_model=Customer)
        self.router.add_api_route("/", self.get_all_customers, methods=["GET"], response_model=List[Customer])
        self.router.add_api_route("/{id}", self.update_customer, methods=["PUT"], response_model=Customer)
        self.router.add_api_route("/{id}", self.delete_customer, methods=["DELETE"])

    async def create_customer(self, customer: CustomerCreate):
        customer_id = self.service.create_customer(customer)
        return {"id": customer_id}

    async def get_customer(self, id: ObjectId):
        customer = self.service.get_customer_by_id(id)
        if customer is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
        return customer

    async def get_all_customers(self):
        return self.service.get_all_customers()

    async def update_customer(self, id: ObjectId, customer: CustomerUpdate):
        updated_customer = self.service.update_customer(id, customer)
        if updated_customer is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
        return updated_customer

    async def delete_customer(self, id: ObjectId):
        success = self.service.delete_customer(id)
        if not success:
            raise HTTPException(status_code=404, detail="Customer not found")
        return {"message": "Customer deleted successfully"}

