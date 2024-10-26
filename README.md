# RESTful API Application

A simple RESTful API application built with Flask, designed to manage user data using MongoDB. This application provides endpoints for user registration, authentication, and CRUD operations.

## API Endpoints

- **POST /users**: Create a new user
- **GET /users**: Retrieve all users
- **GET /users/<user_id>**: Retrieve a specific user by ID
- **PUT /users/<user_id>**: Update user information
- **DELETE /users/<user_id>**: Delete a user
- **POST /auth/login**: Log in a user and receive a JWT
- **POST /auth/refresh**: Refresh the JWT token

## Features

- User registration and login
- JWT authentication for secure access
- CRUD operations for user data
- Error handling and validation with Marshmallow

## Tech Stack

- **Flask**: A lightweight WSGI web application framework for building web applications.
- **Flask-Restful**: An extension for Flask that adds support for quickly building REST APIs.
- **Flask-MongoEngine**: An Object-Document Mapper (ODM) for MongoDB, allowing for easy interaction with the database.
- **Flask-JWT-Extended**: An extension that simplifies the usage of JSON Web Tokens (JWT) for authentication.
- **Marshmallow**: A library for object serialization and deserialization, and for data validation.
- **MongoDB**: A NoSQL database for storing user data.
- **Docker**: Used for containerization to ensure a consistent environment.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pilican142asuflex/RESTFlask.git
   cd RESTFlask
2. **Build and Run with Docker**:
   ```bash
   docker-compose up --build
3. **Access the Application**:
   Once the application is running, you can access the API at http://localhost:<port>(5000)

##Testing
Postman was used to test the API endpoints. You can also use cURL to test the API endpoints.
