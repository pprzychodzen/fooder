from django.db import models
from django.urls import reverse
from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    recipe_category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)

    # user = models.ForeignKey(User, on_delete=models.CASCADE, **NULL_AND_BLANK)

    def get_absolute_url(self):
        return reverse('recipe:detail', kwargs={'id': self.id})

    def __str__(self):
        return self.title
