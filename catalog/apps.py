import posthog
from django.apps import AppConfig

from config.settings import env


class CatalogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "catalog"

    def ready(self):
        posthog.api_key = env("POSTHOG_API_KEY")
        posthog.host = "https://eu.i.posthog.com"
