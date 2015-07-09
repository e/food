from django.shortcuts import render_to_response, get_object_or_404

from recipes.models import Recipe, Tag


def home(request):
    results = {
        'tags': Tag.objects.all(),
        'recipes': Recipe.objects.all()[:5],
    }
    return render_to_response('home.html', results)


def view_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render_to_response('view_recipe.html', {
        'recipe': recipe,
    })

