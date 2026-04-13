namespace Example.Api.Services;

public interface IOrderService
{
    Task<OrderResponse?> GetByIdAsync(Guid orderId, CancellationToken cancellationToken);
    Task<OrderResponse> CreateAsync(CreateOrderRequest request, CancellationToken cancellationToken);
}

public sealed class OrderService : IOrderService
{
    private readonly IOrderRepository _orderRepository;
    private readonly ILogger<OrderService> _logger;

    public OrderService(IOrderRepository orderRepository, ILogger<OrderService> logger)
    {
        _orderRepository = orderRepository;
        _logger = logger;
    }

    public async Task<OrderResponse?> GetByIdAsync(Guid orderId, CancellationToken cancellationToken)
    {
        var order = await _orderRepository.GetByIdAsync(orderId, cancellationToken);
        return order is null ? null : new OrderResponse(order.Id, order.CustomerName, order.TotalAmount);
    }

    public async Task<OrderResponse> CreateAsync(CreateOrderRequest request, CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(request.CustomerName))
        {
            throw new ValidationException("CustomerName is required.");
        }

        var order = new OrderRecord(Guid.NewGuid(), request.CustomerName.Trim(), request.TotalAmount);
        await _orderRepository.AddAsync(order, cancellationToken);

        _logger.LogInformation("Created order {OrderId} for {CustomerName}", order.Id, order.CustomerName);

        return new OrderResponse(order.Id, order.CustomerName, order.TotalAmount);
    }
}
