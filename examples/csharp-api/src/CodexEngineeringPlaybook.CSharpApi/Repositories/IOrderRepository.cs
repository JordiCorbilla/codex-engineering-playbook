using CodexEngineeringPlaybook.CSharpApi.Domain;

namespace CodexEngineeringPlaybook.CSharpApi.Repositories;

public interface IOrderRepository
{
    Task<IReadOnlyList<Order>> ListAsync(CancellationToken cancellationToken);
    Task<Order?> GetByIdAsync(Guid orderId, CancellationToken cancellationToken);
    Task AddAsync(Order order, CancellationToken cancellationToken);
}
