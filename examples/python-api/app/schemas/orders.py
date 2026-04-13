from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


class CreateOrderRequest(BaseModel):
    customer_name: str = Field(min_length=1, max_length=120)
    total_amount: float = Field(ge=0)


class OrderRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    customer_name: str
    total_amount: float
    created_at_utc: datetime

    @classmethod
    def create(cls, customer_name: str, total_amount: float) -> "OrderRecord":
        return cls(
            id=str(uuid4()),
            customer_name=customer_name.strip(),
            total_amount=total_amount,
            created_at_utc=datetime.now(timezone.utc),
        )


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    customer_name: str
    total_amount: float
    created_at_utc: datetime
