from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormMixin
from django.db.models import Q

from main.forms import RecipeCreateForm, CommentForm
from main.models import Recipe, Comment, IngredientsType
from main.filters import RecipeFilter


class RecipeSearchList(ListView):
    model = Recipe
    template_name = 'main/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        return context



# def search_recipe(request):
#     ing1 = IngredientsType.object.get(type='Ingredient1')
#     qs = Recipe.objects.all()
#     ingredients_list = IngredientsType.objects.all()
#     search_result = request.GET.get('ingredient_type')
#
#     qs = qs.filter(search__icontains=search_result)
#     context = {
#         'ingredients_type': ingredients_list,
#         'queryset': qs
#     }
#     return render(request, 'main/search.html', context)


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
