from __future__ import annotations

from dataclasses import dataclass, field

from app.schemas.orders import OrderRecord


class OrderRepository:
    async def list_orders(self) -> list[OrderRecord]:
        raise NotImplementedError

    async def get_by_id(self, order_id: str) -> OrderRecord | None:
        raise NotImplementedError

    async def create(self, order: OrderRecord) -> OrderRecord:
        raise NotImplementedError


@dataclass(slots=True)
class InMemoryOrderRepository(OrderRepository):
    _orders: dict[str, OrderRecord] = field(default_factory=dict)

    async def list_orders(self) -> list[OrderRecord]:
        return sorted(self._orders.values(), key=lambda order: order.created_at_utc, reverse=True)

    async def get_by_id(self, order_id: str) -> OrderRecord | None:
        return self._orders.get(order_id)

    async def create(self, order: OrderRecord) -> OrderRecord:
        self._orders[order.id] = order
        return order
