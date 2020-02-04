from django.shortcuts import render
from django.views.generic import ListView
from main.models import Category


# Create your views here.
def homepage(request):
    return render(request, 'main/home.html')


class CategoryListView(ListView):
    model = Category
    template_name = "main/category.html"
    queryset = Category.objects.all()

