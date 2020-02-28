from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormMixin

from main.forms import RecipeCreateForm, CommentForm
from main.models import Recipe, Comment
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


class RecipeDetail(DetailView, FormMixin):
    model = Recipe
    context_object_name = "recipe"
    template_name = 'main/recipe_detail.html'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid() and len(form.instance.text) > 0:
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.recipe = self.get_object()
        form.save()
        return HttpResponseRedirect(self.request.path_info)


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
