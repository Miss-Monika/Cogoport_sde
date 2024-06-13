# Configuration API

This project is a FastAPI application that provides a Configuration API. The API allows you to manage configurations for different countries.

## Features

- Get configuration for a specific country
- Delete configuration for a specific country
- Root route that redirects to the API documentation

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/configuration-api.git
cd configuration-api
```

## Install the dependencies:


- Running the Application
- You can start the application using Uvicorn, an ASGI server. Run the following command in your terminal:

```bash
uvicorn cogoport.main:app --reload
```
The application will start running at http://127.0.0.1:8000.

## API Endpoints
- GET /: Returns a welcome message and directs you to the API documentation
- DELETE /delete_configuration/{country_code}: Deletes the configuration for the specified country
- GET /get_configuration/{country_code}: Returns the configuration for the specified country
- POST /set_configuration/{country_code}: Sets the configuration for the specified country