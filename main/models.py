from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models
from user.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Sauce(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Serving(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preparing = models.TextField(default="puste przygotowanie")
    recipe_category = models.ForeignKey(Category, default=None, blank=False, on_delete=models.CASCADE,
                                        related_name='category')
    tag = models.ManyToManyField(Tag, blank=True, related_name='recipe_tags')
    ingredients = models.ManyToManyField(Ingredients, blank=True, related_name='recipe_ingredients')
    sauce = models.ManyToManyField(Sauce, blank=True, related_name='recipe_sauce')
    serving = models.ManyToManyField(Serving, blank=True, related_name='recipe_serving')

    image = models.ImageField(upload_to='media', blank=True)

    def get_absolute_url(self):
        return reverse('recipe:detail', kwargs={'id': self.id})

    def __str__(self):
        return self.title


class Comment(models.Model):
    recipe = models.ForeignKey('main.Recipe', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, default=None, blank=False, on_delete=models.CASCADE, null=True,
                               related_name='comment_creator')
    # reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    text = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_date']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
