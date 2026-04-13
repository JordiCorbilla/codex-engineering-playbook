using CodexEngineeringPlaybook.CSharpApi.Models;

namespace CodexEngineeringPlaybook.CSharpApi.Services;

public interface IOrderService
{
    Task<IReadOnlyList<OrderResponse>> ListAsync(CancellationToken cancellationToken);
    Task<OrderResponse> GetByIdAsync(Guid orderId, CancellationToken cancellationToken);
    Task<OrderResponse> CreateAsync(CreateOrderRequest request, CancellationToken cancellationToken);
}
