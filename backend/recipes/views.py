import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .services import search_recipes_by_ingredient, get_recipe_by_id

from .services import search_recipes, format_recipe


@require_GET
def recipe_search(request):
    query = request.GET.get("q", "").strip()

    if not query:
        return JsonResponse(
            {"error": "Enter a recipe name using ?q=chicken"},
            status=400,
        )

    try:
        recipes = search_recipes(query)
        return JsonResponse({
            "recipes": [format_recipe(recipe) for recipe in recipes],
        })
    except (requests.RequestException, ValueError):
        return JsonResponse(
            {"error": "Could not retrieve recipes. Please try again."},
            status=502,
        )
@require_GET
def recipe_ingredient_search(request):
    ingredient = request.GET.get("ingredient", "").strip()

    if not ingredient:
        return JsonResponse(
            {"error": "Enter an ingredient using ?ingredient=chicken"},
            status=400,
        )

    try:
        meals = search_recipes_by_ingredient(ingredient)
        return JsonResponse({
            "recipes": [
                {
                    "id": meal.get("idMeal"),
                    "name": meal.get("strMeal"),
                    "image": meal.get("strMealThumb"),
                }
                for meal in meals
            ],
        })
    except (requests.RequestException, ValueError):
        return JsonResponse(
            {"error": "Could not retrieve recipes. Please try again."},
            status=502,
        )


@require_GET
def recipe_detail(request, recipe_id):
    try:
        recipe = get_recipe_by_id(recipe_id)

        if not recipe:
            return JsonResponse({"error": "Recipe not found."}, status=404)

        return JsonResponse({"recipe": format_recipe(recipe)})
    except (requests.RequestException, ValueError):
        return JsonResponse(
            {"error": "Could not retrieve recipe details. Please try again."},
            status=502,
        )