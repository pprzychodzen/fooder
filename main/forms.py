from django import forms
from main.models import Recipe
from tinymce.widgets import TinyMCE
from django.db import models
from user.models import User


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'recipe_category', 'description']
        category_choices = {'recipe_category': 'Kategorie'}
        # formfield_overrides = {
        #     models.TextField: {'widget': TinyMCE()},
        # }

        recipe_category = forms.ChoiceField(choices=category_choices, label='', initial='Danie główne',
                                            widget=forms.Select(), required=True)
    #
    # class Media:
    #     js = ('/media/tinymce/jscripts/tiny_mce/tiny_mce.js',
    #           '',)
    #
    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user')
    #     super(RecipeCreateForm, self).__init__(*args, **kwargs)
    #
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if Recipe.objects.filter(user=self.user, title=title).exists():
    #         raise forms.ValidationError("You have already written a book with same title.")
    #     return title
