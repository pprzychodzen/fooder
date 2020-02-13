from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from main.forms import RecipeCreateForm
from main.models import Recipe
from main.filters import RecipeFilter


class RecipeListView(ListView):
    model = Recipe
    template_name = "main/home.html"
    queryset = Recipe.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        return context


class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = "recipe"


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    success_url = 'home'
    template_name = 'main/add_recipe.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('homepage')
