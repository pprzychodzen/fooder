from django import forms
from tinymce.widgets import TinyMCE

from main.models import Recipe, Comment


class RecipeCreateForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Recipe
        fields = ['title', 'recipe_category', 'description', 'preparing', 'tag', 'image']
        widgets = {
            'description': TinyMCE(),
        }

    class Media:
        js = ('/media/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': "10", 'rows': '10'}),
        }

