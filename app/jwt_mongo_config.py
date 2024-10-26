import os
from datetime import timedelta

class Config:
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGODB_HOST', 'localhost'),
        'db': 'user_db'
    }
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-jwt-secret-key')
    # JWT token expiration
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)      # Access token expires in 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)     # Refresh token expires in 30 days
