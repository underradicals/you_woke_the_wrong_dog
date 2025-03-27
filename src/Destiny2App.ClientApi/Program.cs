using Destiny2App.Infrastructure;
using FastEndpoints;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFastEndpoints();
builder.Services.AddInfrastructureServices(builder.Configuration);
builder.Services.AddOpenApi();

var app = builder.Build();
app.UseFastEndpoints();
app.UseInfrastructureServices();

if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.Run();

