using CodexEngineeringPlaybook.CSharpApi.Middleware;
using CodexEngineeringPlaybook.CSharpApi.Repositories;
using CodexEngineeringPlaybook.CSharpApi.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSingleton<IOrderRepository, InMemoryOrderRepository>();
builder.Services.AddScoped<IOrderService, OrderService>();
builder.Services.AddControllers();

var app = builder.Build();

app.UseMiddleware<ExceptionMappingMiddleware>();
app.MapControllers();

app.Run();

public partial class Program;
