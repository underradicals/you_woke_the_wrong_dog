# .NET Core Web API - Setup and Build Instructions

## Prerequisites
Ensure you have the following installed on your system:
- **.NET SDK** (Latest stable version) - [Download Here](https://dotnet.microsoft.com/download)
- **Visual Studio** (2022 or later) or **Visual Studio Code** with the C# extension
- **SQL Server** or any other configured database (if applicable)
- **Git** - [Download Here](https://git-scm.com/downloads)

---

## Clone the Repository
```bash
# Using HTTPS
git clone https://github.com/your-repo/Destiny2Ap.git

# Using SSH
git clone git@github.com:your-repo/Destiny2Ap.git
```

Change into the project directory:
```bash
cd Destiny2Ap
```

---

## Configuration
1. **AppSettings Configuration:**
    - Locate the `appsettings.json` file in the `Destiny2Ap.API` directory.
    - Update database connection strings and other environment-specific settings.

2. **Environment Variables:**
    - Optionally, create an `appsettings.Development.json` for local development.
    - Ensure your database credentials and sensitive information are stored securely.

3. **Database Migrations:**
   If using Entity Framework Core:
    ```bash
    dotnet ef database update
    ```
   Ensure `ef` tools are installed using:
    ```bash
    dotnet tool install --global dotnet-ef
    ```

---

## Build the Application
To build the application, run:
```bash
# Build the solution
 dotnet build
```

For a specific project:
```bash
dotnet build Destiny2Ap.API/Destiny2Ap.API.csproj
```

---

## Run the Application
Run the API using the following command:
```bash
# Run using development settings
dotnet run --project Destiny2Ap.API/Destiny2Ap.API.csproj
```
The API should be accessible at `http://localhost:5000` or `https://localhost:5001`.

---

## Testing
Run the tests using the following command:
```bash
# Navigate to the test project directory
cd Destiny2Ap.Tests

# Run tests
dotnet test
```

---

## Additional Commands
- **Clean the Solution:**
  ```bash
  dotnet clean
  ```
- **Restore Packages:**
  ```bash
  dotnet restore
  ```
- **Publish:**
  ```bash
  dotnet publish -c Release -o ./publish
  ```

---

## Troubleshooting
- Ensure your database server is running if applicable.
- Confirm `dotnet` commands are available in your system path.
- Verify that ports 5000 or 5001 are not blocked.
- Check logs for detailed errors: `logs/app.log`

---

## License
This project is licensed under the [Attribution-NonCommercial-NoDerivatives 4.0 International License](LICENSE).


