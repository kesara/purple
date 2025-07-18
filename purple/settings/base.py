# Copyright The IETF Trust 2023-2024, All Rights Reserved
"""Django settings for RPC project common to all environments"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

AUTH_USER_MODEL = "rpcauth.User"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "mozilla_django_oidc",  # load after auth
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_spectacular",
    "rest_framework",
    "rules.apps.AutodiscoverRulesConfig",
    "simple_history",
    "datatracker.apps.DatatrackerConfig",
    "rpc.apps.RpcConfig",
    "rpcauth.apps.RpcAuthConfig",
    "errata.apps.ErrataConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "purple.urls"

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

WSGI_APPLICATION = "purple.wsgi.application"


# Authentication
AUTHENTICATION_BACKENDS = (
    "rpcauth.backends.RpcOIDCAuthBackend",
    "rules.permissions.ObjectPermissionBackend",
    "django.contrib.auth.backends.ModelBackend",  # default backend
)

# OIDC configuration (see also production.py/development.py)
OIDC_RP_SIGN_ALGO = "RS256"
OIDC_RP_SCOPES = "openid profile roles"
OIDC_STORE_ID_TOKEN = True  # store id_token in session (used for RP-initiated logout)
ALLOW_LOGOUT_GET_METHOD = True  # for now anyway
OIDC_OP_LOGOUT_URL_METHOD = "rpcauth.utils.op_logout_url"

# How often to renew tokens? Default is 15 minutes. Needs SessionRefresh middleware.
# OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS = 15 * 60

# Misc
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# django-rest-framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_SCHEMA_CLASS": "purple.openapi.RpcAutoSchema",
}

# DRF OpenApi schema settings
SPECTACULAR_SETTINGS = {
    "TITLE": "Purple",
    "DESCRIPTION": "Backend API for the Purple app",
    "VERSION": "0.1",
    "SCHEMA_PATH_PREFIX": "/api/rpc/",
    "COMPONENT_NO_READ_ONLY_REQUIRED": True,
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Caches - disabled by default, create as appropriate in per-environment config
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# email
EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
