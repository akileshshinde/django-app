from django.apps import AppConfig


class MyAppConfig(AppConfig):  # Change the class name to something unique
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'  # Ensure this matches the actual app folder name
