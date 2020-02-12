from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    preparing = models.TextField(default="pusty")
    recipe_category = models.ForeignKey(Category, default=None, blank=False, on_delete=models.CASCADE,
                                        related_name='category')
    tag = models.ManyToManyField(Tag, blank=True, related_name='recipe_tags')

    def get_absolute_url(self):
        return reverse('recipe:detail', kwargs={'id': self.id})

    def __str__(self):
        return self.title
