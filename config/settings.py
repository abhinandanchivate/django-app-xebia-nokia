# host related details , installed app info, middleware, jwt related info, root router info , timezeone,permissions related stuff , logging related stuff, etc.
import os 
from pathlib import Path

# base directory
BASE_DIR = Path(__file__).resolve().parent.parent
# secret key
SECRET_KEY = os.getenv('SECRET_KEY','dev_secret_key')
#Fetches SECRET_KEY from the environment. Falls back to "dev_secret_key" if not found.
# debug mode
DEBUG = True
# DEBUG = True : will set it False in production
# allowed hosts
ALLOWED_HOSTS = ['*']  # '*' allows all hosts, change this in production if u are expecting a specific hosts then instead of * provide the details 
# installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
    'corsheaders',  # CORS headers
    'apps.users',
    'apps.roles',
    'apps.assets'  # our custom apps for roles, account , assets

]
# middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS headers
    #authentication middleware
    'django.middleware.common.CommonMiddleware',
    #CSRF : cross site request forgery
    # This middleware is used to protect against CSRF attacks by ensuring that requests made to the server are from authenticated users.
    # its an attak where a malicious website tricks a user into submitting a request to another site where they are authenticated.
    # it will bring the token from the user session and check if the request is valid or not

    'django.middleware.csrf.CsrfViewMiddleware',#CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
# root url configuration
ROOT_URLCONF = 'config.urls'
# WSGI compatibility for the servers like gunicorn, uWSGI, etc.
# WSGI stands for Web Server Gateway Interface, which is a specification that allows web servers to communicate with web applications.
WSGI_APPLICATION = 'config.wsgi.application'
# PostgreSQL database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",#
        "NAME": os.getenv('POSTGRES_DB', 'test_db'),
        "USER": os.getenv('POSTGRES_USER', 'test_user'),
        "PASSWORD": os.getenv('POSTGRES_PASSWORD', 'test_password'),
        "HOST": os.getenv('POSTGRES_HOST', 'localhost'),
        "PORT": os.getenv('POSTGRES_PORT', '5432'),
    }

}
# mongodb configuration settings==> mongodb we will write it manually
MONGODB_SETTINGS = {
    "NAME": os.getenv('MONGO_DB', 'test_db'),
    "HOST": os.getenv('MONGO_HOST', 'localhost'),
    "PORT": os.getenv('MONGO_PORT', '27017'),
    "USERNAME": os.getenv('MONGO_USER', 'test_user'),
    "PASSWORD": os.getenv('MONGO_PASSWORD', 'test_password'),
    "AUTH_SOURCE": os.getenv('MONGO_AUTH_DB', 'admin'),
}

#Language code
LANGUAGE_CODE = 'en-us'
# Time zone
TIME_ZONE = 'UTC'
# Use i18N
USE_I18N = True
# enables timezone aware datetimes
USE_TZ = True
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.JWTAuthentication',  # JWT authentication
        # custom RBAC permissions
       
    ),
    'DEFAULT_PERMISSION_CLASSES': (
         'rest_framework.permissions.Allowany', 
    ),
}

os.makedirs(os.path.join(BASE_DIR, 'logs'), exist_ok=True)  # Ensure logs directory exists

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'api.log'),
            'formatter': 'verbose',
        },
    },
}






