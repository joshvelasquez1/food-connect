import requests


def search_recipes(name):
    response = requests.get(
        "https://www.themealdb.com/api/json/v1/1/search.php",
        params={"s": name},
        timeout=15,
    )
    response.raise_for_status()
    return response.json().get("meals") or []


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
                print(f"\n{recipe['strMeal']}")
                print("Ingredients:")

                for number in range(1, 21):
                    ingredient = (
                        recipe.get(f"strIngredient{number}") or ""
                    ).strip()
                    measure = (
                        recipe.get(f"strMeasure{number}") or ""
                    ).strip()

                    if ingredient:
                        print(f"- {measure} {ingredient}".strip())

        except (requests.RequestException, ValueError):
            print("Could not retrieve recipes. Please try again.")