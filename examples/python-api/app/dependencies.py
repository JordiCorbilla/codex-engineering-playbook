from app.data.orders import InMemoryOrderRepository
from app.services.orders import OrderService

_repository = InMemoryOrderRepository()


def get_order_service() -> OrderService:
    return OrderService(repository=_repository)
