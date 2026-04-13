from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_order_service
from app.schemas.orders import CreateOrderRequest, OrderResponse
from app.services.orders import OrderNotFoundError, OrderService

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id: str,
    service: OrderService = Depends(get_order_service),
) -> OrderResponse:
    try:
        return await service.get_order(order_id)
    except OrderNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
    request: CreateOrderRequest,
    service: OrderService = Depends(get_order_service),
) -> OrderResponse:
    return await service.create_order(request)
