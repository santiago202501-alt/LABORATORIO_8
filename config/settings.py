import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar las variables de entorno desde el archivo .env
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = "django-insecure-classroomhub-development-only"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "3306"),
        "OPTIONS": {
            "charset": "utf8mb4",
        },
        "TEST": {
            "NAME": "test_classroom_hub",
        },
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Autenticación (Laboratorio 8): se usan nombres de ruta, no URL escritas a mano.
LOGIN_URL = "pages:login"
LOGIN_REDIRECT_URL = "pages:dashboard"
LOGOUT_REDIRECT_URL = "pages:home"

# ---------------------------------------------------------------------------
# Compatibilidad OPCIONAL con MariaDB 10.4 (por ejemplo, el de XAMPP).
#
# Django 6.1 exige MariaDB 10.11+ (Django 5.2 LTS, 10.5+). Este parche engaña
# a Django con la version del servidor y desactiva INSERT ... RETURNING. No es
# una configuracion soportada: la solucion correcta es actualizar el servidor.
# Solo se activa si MARIADB_COMPAT_104=1 en el archivo .env.
# ---------------------------------------------------------------------------
if os.getenv("MARIADB_COMPAT_104", "0") == "1":
    from django.db.backends.mysql.base import DatabaseWrapper
    from django.db.backends.mysql.features import DatabaseFeatures

    DatabaseWrapper.get_database_version = lambda self: (10, 11, 0)
    DatabaseFeatures.can_return_columns_from_insert = False
