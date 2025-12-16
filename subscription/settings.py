from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-change-this-in-production"

DEBUG = True

ALLOWED_HOSTS = []

# ---------------- APPS ----------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "subscribe",
]

# ---------------- MIDDLEWARE ----------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "subscription.urls"

# ---------------- TEMPLATES ----------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ---------------- DATABASE ----------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ---------------- STATIC ----------------

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Required for development
STATIC_ROOT = BASE_DIR / "staticfiles"

# ---------------- AUTH ----------------
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/login/"

# =================== SQUARE SANDBOX ===================
# THESE VALUES COME FROM SQUARE DASHBOARD (SANDBOX)

SQUARE_ENVIRONMENT = "sandbox"
SQUARE_ACCESS_TOKEN = "sandbox-sq0idb-4nZcWFEMK8jgjsNBF91hXA"
SQUARE_LOCATION_ID = "EAAAl6_34kUVyjBj2z_5UuPROzlhEW_SQVWrfPX50FpcKXNeUSZViXrwq6EXjKV7"
SQUARE_API_BASE ="https://connect.squareupsandbox.com"



# ======================================================
