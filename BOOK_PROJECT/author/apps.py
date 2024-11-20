from django.apps import AppConfig


class MovieConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "author"
    verbose_name="作者"  #修改应用名
