from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ... existing code ...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ... other middleware ...
]

# ... existing code ...

# Database
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'resume_me_db',
        'CLIENT': {
            'host': os.getenv('MONGODB_URI'),
        }
    }
}

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True  # For development, restrict this in production

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')