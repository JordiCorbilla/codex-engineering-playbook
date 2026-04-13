from dataclasses import dataclass

from app.data.orders import OrderRepository
from app.schemas.orders import CreateOrderRequest, OrderResponse


class OrderNotFoundError(Exception):
    pass


@dataclass(slots=True)
class OrderService:
    repository: OrderRepository

    async def get_order(self, order_id: str) -> OrderResponse:
        order = await self.repository.get_by_id(order_id)
        if order is None:
            raise OrderNotFoundError(f"Order '{order_id}' was not found.")
        return OrderResponse.model_validate(order)

    async def create_order(self, request: CreateOrderRequest) -> OrderResponse:
        created = await self.repository.create(request)
        return OrderResponse.model_validate(created)
