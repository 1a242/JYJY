from django.db import models
from django.contrib.auth.models import User

class Book(models.Model) :
    title = models.CharField(max_length=100, default=" ", verbose_name="书籍名")
    authors = models.CharField(max_length=64, default=" ", verbose_name="作者")
    publisher = models.CharField(max_length=254, default=" ", verbose_name="出版社")
    description = models.CharField(max_length=1000, default=" ", verbose_name="书籍简介")
    image = models.ImageField(upload_to='book/images/', verbose_name="书籍封面")
    url = models.URLField(blank=True, verbose_name="书籍资源链接")

    class Meta:
        verbose_name = "图书管理"
        verbose_name_plural = "书籍列表"
    def __str__(self):
        return self.title

class Review2(models. Model) :
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self) :
        return self.text
