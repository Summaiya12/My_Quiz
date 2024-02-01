from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default="")

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, null=True)
    opt1 = models.CharField(max_length=200, null=True)
    opt2 = models.CharField(max_length=200, null=True)
    opt3 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    time = models.IntegerField(default=False)

    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question
