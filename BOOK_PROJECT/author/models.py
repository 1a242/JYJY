from django.db import models
from django.contrib.auth.models import User

class Author(models.Model) :
    name = models.CharField(max_length=200, default=" ", verbose_name="作者名")
    sex = models.CharField(max_length=50, default=" ", verbose_name='性别')
    description = models.CharField(max_length=500, default=" ", verbose_name="作者简介")
    birthdata = models.IntegerField(default=" ", verbose_name="出生日期")
    image = models.ImageField(upload_to='author/images/', verbose_name='作者封面')
    works = models.CharField(max_length=200, default=" ", verbose_name="作品")
# Create your models here.
    class Meta:
        verbose_name="作者"
        verbose_name_plural="作者"

    def __str__(self):
        return self.name
class Review1(models. Model) :
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self) :
        return self.text
