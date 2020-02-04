from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
