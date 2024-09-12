from typing import Optional, List

from pymongo.collection import Collection
from pymongo.database import Database

from common.fields.object_id import ObjectId
from customer.customer_model import Customer, CustomerUpdate, CustomerCreate


class CustomerRepository:
    def __init__(self, db: Database):
        self.collection: Collection = db.get_collection('customers')

    def create_customer(self, customer: CustomerCreate) -> ObjectId:
        result = self.collection.insert_one(customer.model_dump(by_alias=True, exclude_none=True))
        return ObjectId(result.inserted_id)

    def get_customer_by_id(self, id: ObjectId) -> Optional[Customer]:
        result = self.collection.find_one({"_id": id})
        if result:
            return Customer(**result)
        return None

    def get_all_customers(self) -> List[Customer]:
        result = self.collection.find()
        customers = [Customer(**x) for x in result]
        return customers

    def update_customer(self, id: ObjectId, customer: CustomerUpdate) -> Optional[Customer]:
        result = self.collection.update_one({"_id": id}, {"$set": customer.model_dump(by_alias=True, exclude_none=True)})
        if result.modified_count:
            return self.get_customer_by_id(id)
        return None

    def delete_customer(self, id: ObjectId) -> bool:
        result = self.collection.delete_one({"_id": id})
        return result.deleted_count == 1