using System.Collections.Concurrent;
using CodexEngineeringPlaybook.CSharpApi.Domain;

namespace CodexEngineeringPlaybook.CSharpApi.Repositories;

public sealed class InMemoryOrderRepository : IOrderRepository
{
    private readonly ConcurrentDictionary<Guid, Order> _orders = new();

    public Task<IReadOnlyList<Order>> ListAsync(CancellationToken cancellationToken)
    {
        IReadOnlyList<Order> orders = _orders.Values
            .OrderByDescending(order => order.CreatedAtUtc)
            .ToList();

        return Task.FromResult(orders);
    }

    public Task<Order?> GetByIdAsync(Guid orderId, CancellationToken cancellationToken)
    {
        _orders.TryGetValue(orderId, out var order);
        return Task.FromResult(order);
    }

    public Task AddAsync(Order order, CancellationToken cancellationToken)
    {
        _orders[order.Id] = order;
        return Task.CompletedTask;
    }
}
