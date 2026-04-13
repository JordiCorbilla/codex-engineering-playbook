from pydantic import BaseModel, Field


class CreateOrderRequest(BaseModel):
    customer_name: str = Field(min_length=1, max_length=120)
    total_amount: float = Field(ge=0)


class OrderResponse(BaseModel):
    id: str
    customer_name: str
    total_amount: float
