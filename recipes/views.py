from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from recipes.models import Recipe

def index(request):
    recipes = Recipe.objects.all()
    return render_to_response('recipes/index.html', {'object_list': recipes})


def detail(request, slug):
	recipe = get_object_or_404(Recipe, slug=slug)
	return render_to_response('recipes/detail.html', {'object': recipe})
