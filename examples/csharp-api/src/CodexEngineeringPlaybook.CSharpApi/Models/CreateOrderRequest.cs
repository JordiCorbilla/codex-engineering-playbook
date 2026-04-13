using System.ComponentModel.DataAnnotations;

namespace CodexEngineeringPlaybook.CSharpApi.Models;

public sealed record CreateOrderRequest(
    [property: Required, StringLength(120, MinimumLength = 1)] string CustomerName,
    [property: Range(typeof(decimal), "0", "79228162514264337593543950335")] decimal TotalAmount);
