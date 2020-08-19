from django.contrib import admin
from .models import Category, Recipe, Tag, Comment, Ingredients, Sauce, Serving, IngredientsType
from tinymce.widgets import TinyMCE
from django.db import models


class RecipeAdmin(admin.ModelAdmin):
    fields = ["title",
              "recipe_category",
              "description",
              "preparing",
              "tag",
              "ingredients_type",
              "ingredients",
              "sauce",
              "serving",
              "image"]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Sauce)
admin.site.register(Serving)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Ingredients)
admin.site.register(IngredientsType)
