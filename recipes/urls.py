from django.conf.urls import patterns, include, url

from recipes.views import RecipeDetailView, RecipeListView

urlpatterns = patterns('recipes.views',
    url(r'^add/$', 'add', name='recipes_recipe_add'),
    url(r'^edit/(?P<recipe_id>\d+)/$', 'edit', name='recipes_recipe_edit'),
)

urlpatterns += patterns('',
	url(r'^recipes/(?P<slug>[-\w]+)/$', RecipeDetailView.as_view(),
		name='recipes_recipe_detail'),
	url(r'^$', RecipeListView.as_view(), name='recipes_recipe_index'),
)
