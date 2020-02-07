from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    DINNER = 'Danie główne'
    SUPPER = 'Kolacja'
    DESSERT = 'Deser'
    STARTER = 'Przystawka'
    category_choices = [
        (DINNER, 'Danie główne'),
        (SUPPER, 'Kolacja'),
        (DESSERT, 'Deser'),
        (STARTER, 'Przystawka'),

    ]

    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    recipe_category = models.CharField(max_length=30, choices=category_choices, default=DINNER)

    def get_absolute_url(self):
        return reverse('recipe:detail', kwargs={'id': self.id})

    def __str__(self):
        return self.title
