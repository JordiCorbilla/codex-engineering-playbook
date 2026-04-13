namespace CodexEngineeringPlaybook.CSharpApi.Models;

public sealed record OrderResponse(
    Guid Id,
    string CustomerName,
    decimal TotalAmount,
    DateTimeOffset CreatedAtUtc);
