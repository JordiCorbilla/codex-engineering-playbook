namespace Example.Api.Repositories;

public sealed class OrderRepository : IOrderRepository
{
    private readonly AppDbContext _dbContext;

    public OrderRepository(AppDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public Task<OrderRecord?> GetByIdAsync(Guid orderId, CancellationToken cancellationToken)
    {
        return _dbContext.Orders
            .AsNoTracking()
            .SingleOrDefaultAsync(order => order.Id == orderId, cancellationToken);
    }

    public async Task AddAsync(OrderRecord order, CancellationToken cancellationToken)
    {
        _dbContext.Orders.Add(order);
        await _dbContext.SaveChangesAsync(cancellationToken);
    }
}
