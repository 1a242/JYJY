from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "book"
    verbose_name="书籍"  #修改应用名