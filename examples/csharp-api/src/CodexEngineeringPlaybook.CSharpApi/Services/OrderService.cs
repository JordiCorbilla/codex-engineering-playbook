using System.ComponentModel.DataAnnotations;
using CodexEngineeringPlaybook.CSharpApi.Domain;
using CodexEngineeringPlaybook.CSharpApi.Errors;
using CodexEngineeringPlaybook.CSharpApi.Models;
using CodexEngineeringPlaybook.CSharpApi.Repositories;

namespace CodexEngineeringPlaybook.CSharpApi.Services;

public sealed class OrderService : IOrderService
{
    private readonly IOrderRepository _repository;
    private readonly ILogger<OrderService> _logger;

    public OrderService(IOrderRepository repository, ILogger<OrderService> logger)
    {
        _repository = repository;
        _logger = logger;
    }

    public async Task<IReadOnlyList<OrderResponse>> ListAsync(CancellationToken cancellationToken)
    {
        var orders = await _repository.ListAsync(cancellationToken);
        return orders.Select(Map).ToList();
    }

    public async Task<OrderResponse> GetByIdAsync(Guid orderId, CancellationToken cancellationToken)
    {
        var order = await _repository.GetByIdAsync(orderId, cancellationToken);
        if (order is null)
        {
            throw new OrderNotFoundException(orderId);
        }

        return Map(order);
    }

    public async Task<OrderResponse> CreateAsync(CreateOrderRequest request, CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(request.CustomerName))
        {
            throw new ValidationException("CustomerName is required.");
        }

        if (request.TotalAmount < 0)
        {
            throw new ValidationException("TotalAmount must be greater than or equal to zero.");
        }

        var order = new Order(
            Guid.NewGuid(),
            request.CustomerName.Trim(),
            request.TotalAmount,
            DateTimeOffset.UtcNow);

        await _repository.AddAsync(order, cancellationToken);
        _logger.LogInformation("Created order {OrderId} for {CustomerName}", order.Id, order.CustomerName);

        return Map(order);
    }

    private static OrderResponse Map(Order order)
    {
        return new OrderResponse(order.Id, order.CustomerName, order.TotalAmount, order.CreatedAtUtc);
    }
}
