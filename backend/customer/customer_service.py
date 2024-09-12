from typing import Optional, List

from common.fields.object_id import ObjectId
from customer.customer_dtos import CreateCustomerData, UpdateCustomerData
from customer.customer_model import Customer
from customer.customer_repository import CustomerRepository


class CustomerService:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def create_customer(self, customer_data: CreateCustomerData) -> ObjectId:
        return self.customer_repository.create_customer(customer_data)

    def get_customer_by_id(self, id: ObjectId) -> Optional[Customer]:
        return self.customer_repository.get_customer_by_id(id)

    def get_all_customers(self) -> List[Customer]:
        return self.customer_repository.get_all_customers()

    def update_customer(self, id: ObjectId, customer_data: UpdateCustomerData) -> Optional[Customer]:
        return self.customer_repository.update_customer(id, customer_data)

    def delete_customer(self, id: ObjectId) -> bool:
        return self.customer_repository.delete_customer(id)
