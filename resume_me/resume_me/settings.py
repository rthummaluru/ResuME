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

# Add OpenAI API key
OPENAI_API_KEY = 'your_openai_api_key_here'