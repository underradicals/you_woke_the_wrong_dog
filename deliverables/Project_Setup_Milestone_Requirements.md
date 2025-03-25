## Project Setup Milestone Requirements

### **1. Project Initialization**
- Scaffold a .NET Core project using Clean Architecture principles with the following layers:
    - **Domain**: Contains entities, value objects, and domain services.
    - **Application**: Contains use cases, DTOs, and interfaces.
    - **Infrastructure**: Responsible for external concerns like database access, logging, and API integration.
    - **Presentation**: Contains controllers and endpoints (if using an API).
- Ensure proper namespace conventions are followed.
- Verify all projects build successfully.

### **2. Environment Setup**
- Install the necessary .NET SDK version.
- Configure an IDE (e.g., Visual Studio, Visual Studio Code).
- Install required dependencies using NuGet.
- Create a `README.md` with build and run instructions.

### **3. Version Control**
- Initialize a Git repository for source control.
- Add a `.gitignore` file for .NET projects using the standard template.
- Commit the initial project structure.
- Create meaningful branches (e.g., `main`, `develop`, `feature/logging`).

### **4. Logging Setup**
- Install Serilog and Serilog sinks for file and console logging using NuGet.
- Implement structured logging.
- Configure rolling log files by log level (e.g., Information, Warning, Error).
- Implement an `ILoggerService` interface in the **Application** layer.
- Create a `LoggerService` class in the **Infrastructure** layer to handle logging.
- Configure logging options in `appsettings.json` with appropriate parameters for:
    - File paths.
    - Retention policies.
    - Log level controls.
- Verify logs are written to appropriate files and displayed on the console.

### **5. MediatR Setup**
- Install MediatR and MediatR.Extensions.Microsoft.DependencyInjection using NuGet.
- Create a pipeline behavior for logging requests, responses, and exceptions.
- Ensure logs include relevant information like timestamps, correlation IDs, and exceptions.

### **6. Basic API and Logging Verification**
- Create a sample API endpoint in the **Presentation** layer.
- Implement a simple Application layer use case to be triggered by the endpoint.
- Log the incoming requests, outgoing responses, and any exceptions using the configured logging pipeline.
- Validate the following scenarios:
    - Successful API request with Information logs.
    - API request with a handled exception producing an Error log.
    - Warning logs for any application-specific warnings.

### **7. Configuration Management**
- Create configuration settings for different environments (`appsettings.Development.json`, `appsettings.Production.json`).
- Ensure Serilog uses the correct configuration based on the environment.

### **8. Documentation**
- Document the project structure, explaining how Clean Architecture is applied.
- Provide detailed instructions on how to:
    - Configure logging.
    - Add new pipeline behaviors.
    - Interpret log files.
- Add an example of a typical log entry for easy debugging.

### **9. Acceptance Criteria**
- The project builds and runs successfully.
- API requests are logged using structured logging.
- Logs are stored in separate rolling files according to log levels.
- Console logging works without errors.
- MediatR pipeline behavior logs request, response, and exceptions correctly.
- Documentation is clear and complete.

