from django.contrib import admin
from .models import Category, Recipe, Tag

# Register your models here.


admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Tag)
