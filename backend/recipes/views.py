import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET

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