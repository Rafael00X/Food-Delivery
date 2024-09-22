from pydantic import BaseModel, Field
from typing import Optional


class Address(BaseModel):
    street: str = Field(..., description="The street address")
    city: str = Field(..., description="The city of the address")
    state: str = Field(..., description="The state of the address")
    postal_code: str = Field(..., description="The postal or ZIP code")
    country: Optional[str] = Field("USA", description="The country of the address, default is USA")

    class Config:
        schema_extra = {
            "example": {
                "street": "123 Main St",
                "city": "Springfield",
                "state": "IL",
                "postal_code": "62704",
                "country": "USA"
            }
        }
