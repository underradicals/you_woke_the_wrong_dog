using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Serilog;

namespace Destiny2App.Infrastructure;

public static class Infrastructure_DI_Extensions
{
    public static IServiceCollection AddInfrastructureServices(this IServiceCollection services, IConfiguration configuration)
    {

        AddDestiny2Logging(services, configuration);
        return services;
    }

    public static WebApplication UseInfrastructureServices(this WebApplication app)
    {
        UseDestiny2Logging(app);
        return app;
    }

    private static void AddDestiny2Logging(IServiceCollection services, IConfiguration configuration)
    {
        services.AddSerilog((a, b) =>
        {
            b.ReadFrom.Configuration(configuration);
            b.ReadFrom.Services(a);
        });
    }

    private static void UseDestiny2Logging(WebApplication app)
    {
        app.UseSerilogRequestLogging();
    }
}