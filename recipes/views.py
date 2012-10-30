from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from recipes.models import Recipe
from recipes.forms import RecipeForm

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html',	
		{'object_list': recipes})


def detail(request, slug):
	recipe = get_object_or_404(Recipe, slug=slug)
	return render(request, 'recipes/detail.html', 
		{'object': recipe})
		
@login_required
def add(request):
	if request.method == 'POST':
		form = RecipeForm(user=request.user, data=request.POST)
		if form.is_valid():
			recipe=form.save()
			return HttpResponseRedirect(recipe.get_absolute_url())
	else:
		form = RecipeForm()
	return render(request, 'recipes/form.html',
		{'form': form, 'add': True})

@login_required
def edit(request, recipe_id):
	recipe = get_object_or_404(Recipe, pk=recipe_id)
	if recipe.author != request.user and not request.user.is_staff:
		return HttpResponseForbidden()
	if request.method == 'POST':
		form = RecipeForm(instance=recipe, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(recipe.get_absolute_url())
	else:
		form = RecipeForm(instance=recipe)
	return render(request, 'recipes/form.html',
		{'form': form, 'add': False, 'object': recipe})
