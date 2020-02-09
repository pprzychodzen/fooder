from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from main.forms import RecipeCreateForm
from main.models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = "main/home.html"
    queryset = Recipe.objects.all()
    paginate_by = 10


class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = "recipe"


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'main/add_recipe.html'
    form_class = RecipeCreateForm
    success_url = 'home'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('homepage')
