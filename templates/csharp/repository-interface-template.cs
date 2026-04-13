namespace Example.Api.Repositories;

public interface IOrderRepository
{
    Task<OrderRecord?> GetByIdAsync(Guid orderId, CancellationToken cancellationToken);
    Task AddAsync(OrderRecord order, CancellationToken cancellationToken);
}
