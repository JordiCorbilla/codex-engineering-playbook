using Microsoft.AspNetCore.Mvc;

namespace Example.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public sealed class OrdersController : ControllerBase
{
    private readonly IOrderService _orderService;

    public OrdersController(IOrderService orderService)
    {
        _orderService = orderService;
    }

    [HttpGet("{orderId:guid}")]
    public async Task<ActionResult<OrderResponse>> GetByIdAsync(
        Guid orderId,
        CancellationToken cancellationToken)
    {
        var order = await _orderService.GetByIdAsync(orderId, cancellationToken);

        return order is null ? NotFound() : Ok(order);
    }

    [HttpPost]
    public async Task<ActionResult<OrderResponse>> CreateAsync(
        [FromBody] CreateOrderRequest request,
        CancellationToken cancellationToken)
    {
        var order = await _orderService.CreateAsync(request, cancellationToken);

        return CreatedAtAction(nameof(GetByIdAsync), new { orderId = order.Id }, order);
    }
}
