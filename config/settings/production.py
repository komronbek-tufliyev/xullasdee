from .base import env

DATABASES = {
    # amazon s3 bucket
    "default": {
        # configured for mysql database
        "ENGINE": 'django.db.backends.mysql',
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASSWORD"),
        "HOST": "localhost",# env.str("DB_HOST")        
        "PORT": 5432, # env.str("DB_PORT"),
        "ATOMIC_REQUESTS": True,
        
    }
}