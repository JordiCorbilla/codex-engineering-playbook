using CodexEngineeringPlaybook.CSharpApi.Models;
using CodexEngineeringPlaybook.CSharpApi.Services;
using Microsoft.AspNetCore.Mvc;

namespace CodexEngineeringPlaybook.CSharpApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public sealed class OrdersController : ControllerBase
{
    private readonly IOrderService _service;

    public OrdersController(IOrderService service)
    {
        _service = service;
    }

    [HttpGet]
    public async Task<ActionResult<IReadOnlyList<OrderResponse>>> ListAsync(CancellationToken cancellationToken)
    {
        var orders = await _service.ListAsync(cancellationToken);
        return Ok(orders);
    }

    [HttpGet("{orderId:guid}")]
    public async Task<ActionResult<OrderResponse>> GetByIdAsync(Guid orderId, CancellationToken cancellationToken)
    {
        var order = await _service.GetByIdAsync(orderId, cancellationToken);
        return Ok(order);
    }

    [HttpPost]
    public async Task<ActionResult<OrderResponse>> CreateAsync(
        [FromBody] CreateOrderRequest request,
        CancellationToken cancellationToken)
    {
        var order = await _service.CreateAsync(request, cancellationToken);
        return CreatedAtAction(nameof(GetByIdAsync), new { orderId = order.Id }, order);
    }
}
