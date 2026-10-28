import requests


def search_recipes(name):
    response = requests.get(
        "https://www.themealdb.com/api/json/v1/1/search.php",
        params={"s": name},
        timeout=15,
    )
    response.raise_for_status()
    return response.json().get("meals") or []
def search_recipes_by_ingredient(ingredient):
    response = requests.get(
        "https://www.themealdb.com/api/json/v1/1/filter.php",
        params={"i": ingredient},
        timeout=15,
    )
    response.raise_for_status()
    return response.json().get("meals") or []
def get_recipe_by_id(recipe_id):
    response = requests.get(
        "https://www.themealdb.com/api/json/v1/1/lookup.php",
        params={"i": recipe_id},
        timeout=15,
    )
    response.raise_for_status()

    recipes = response.json().get("meals") or []
    return recipes[0] if recipes else None
def format_recipe(recipe):
    ingredients = []

    for number in range(1, 21):
        ingredient = (recipe.get(f"strIngredient{number}") or "").strip()
        measure = (recipe.get(f"strMeasure{number}") or "").strip()

        if ingredient:
            ingredients.append({
                "name": ingredient,
                "measure": measure,
            })

    return {
        "id": recipe.get("idMeal"),
        "name": recipe.get("strMeal"),
        "category": recipe.get("strCategory"),
        "area": recipe.get("strArea"),
        "image": recipe.get("strMealThumb"),
        "instructions": recipe.get("strInstructions"),
        "ingredients": ingredients,
    }


if __name__ == "__main__":
    search = input("Search for a recipe: ").strip()

    if not search:
        print("Please enter a recipe name.")
    else:
        try:
            recipes = search_recipes(search)

            if not recipes:
                print("No recipes found.")

            for recipe in recipes[:5]:
                formatted_recipe = format_recipe(recipe)
                print(f"\n{formatted_recipe['name']}")
                print("Ingredients:")

                for ingredient in formatted_recipe['ingredients']:
                    print(f"- {ingredient['measure']} {ingredient['name']}")
                    
        except (requests.RequestException, ValueError):
            print("Could not retrieve recipes. Please try again.")