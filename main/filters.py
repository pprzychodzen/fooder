import django_filters
from django.forms.widgets import TextInput

from main.models import Recipe


class RecipeFilter(django_filters.FilterSet):
    # title = django_filters.CharFilter(label="", lookup_expr='icontains',
    #                                   widget=TextInput(attrs={'placeholder': 'szukaj przepisu'}))

    class Meta:
        model = Recipe
        fields = ['ingredients_type']
