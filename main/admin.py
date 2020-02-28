from django.contrib import admin
from .models import Category, Recipe, Tag, Comment
from tinymce.widgets import TinyMCE
from django.db import models


class Admin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},

    }


admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Comment)
