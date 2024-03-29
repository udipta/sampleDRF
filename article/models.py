from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,related_name='articles')

    def __str__(self):
        return self.title
