INSTALLED_APPS = [
    # ...
    'rest_framework',
    'corsheaders',
    'resume_api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ... other middleware
]

CORS_ALLOW_ALL_ORIGINS = True  # For development only, restrict in production

# Add MongoDB settings
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'resume_db',
        'CLIENT': {
            'host': 'mongodb://localhost:27017',
        }
    }
}


DEBUG = False  # Ensure this is set to False for production

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Add your domain names here