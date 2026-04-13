namespace CodexEngineeringPlaybook.CSharpApi.Domain;

public sealed record Order(
    Guid Id,
    string CustomerName,
    decimal TotalAmount,
    DateTimeOffset CreatedAtUtc);
