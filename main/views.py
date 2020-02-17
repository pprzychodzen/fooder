from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from main.forms import RecipeCreateForm
from main.models import Recipe
from main.filters import RecipeFilter


def search(request):
    recipe_list = Recipe.objects.all()
    recipe_filter = RecipeFilter(request.GET, queryset=recipe_list)
    return render(request, 'main/search.html', {'filter': recipe_filter})


class RecipeListView(ListView):
    model = Recipe
    template_name = "main/home.html"
    context_object_name = 'recipes'
    queryset = Recipe.objects.all()
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecipeFilter(self.request.GET, queryset=Recipe.objects.all())
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
