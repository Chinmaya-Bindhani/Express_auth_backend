from .base import *
import os
import environ
import dj_database_url


env = environ.Env()

environ.Env.read_env(BASE_DIR / ".env")



BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = env.bool("DEBUG", default=False)

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
ALLOWED_HOSTS = os.environ["DJANGO_ALLOWED_HOSTS"].split(",")

DATABASES = {
    "default": dj_database_url.parse(
        os.environ["DATABASE_URL"],
        conn_max_age=600,
        conn_health_checks=True,
    )
}
