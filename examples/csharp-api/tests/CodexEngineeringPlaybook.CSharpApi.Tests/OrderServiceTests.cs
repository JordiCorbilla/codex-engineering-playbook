using CodexEngineeringPlaybook.CSharpApi.Errors;
using CodexEngineeringPlaybook.CSharpApi.Models;
using CodexEngineeringPlaybook.CSharpApi.Repositories;
using CodexEngineeringPlaybook.CSharpApi.Services;
using Microsoft.Extensions.Logging.Abstractions;
using Xunit;

namespace CodexEngineeringPlaybook.CSharpApi.Tests;

public sealed class OrderServiceTests
{
    [Fact]
    public async Task CreateAsync_PersistsAndReturnsOrder()
    {
        var repository = new InMemoryOrderRepository();
        var service = new OrderService(repository, NullLogger<OrderService>.Instance);

        var created = await service.CreateAsync(new CreateOrderRequest("Acme Corp", 42.5m), CancellationToken.None);

        Assert.Equal("Acme Corp", created.CustomerName);
        Assert.Equal(42.5m, created.TotalAmount);

        var stored = await service.GetByIdAsync(created.Id, CancellationToken.None);
        Assert.Equal(created.Id, stored.Id);
    }

    [Fact]
    public async Task GetByIdAsync_ThrowsForUnknownOrder()
    {
        var repository = new InMemoryOrderRepository();
        var service = new OrderService(repository, NullLogger<OrderService>.Instance);

        await Assert.ThrowsAsync<OrderNotFoundException>(() =>
            service.GetByIdAsync(Guid.NewGuid(), CancellationToken.None));
    }
}
