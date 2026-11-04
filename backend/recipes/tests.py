from unittest.mock import patch

import requests
from django.test import SimpleTestCase


class RecipeAPITests(SimpleTestCase):
    def setUp(self):
        self.meal = {
            "idMeal": "52777",
            "strMeal": "Pasta Salad",
            "strIngredient1": "Pasta",
            "strMeasure1": "200 g",
        }

    @patch("recipes.views.search_recipes")
    def test_name_search(self, mock_search):
        mock_search.return_value = [self.meal]

        response = self.client.get(
            "/api/recipes/search/", {"q": "pasta"}
        )

        self.assertEqual(response.status_code, 200)
        recipe = response.json()["recipes"][0]
        self.assertEqual(recipe["name"], "Pasta Salad")
        self.assertEqual(
            recipe["ingredients"],
            [{"name": "Pasta", "measure": "200 g"}],
        )
        mock_search.assert_called_once_with("pasta")

    def test_missing_search_input(self):
        for url in (
            "/api/recipes/search/",
            "/api/recipes/ingredient/",
        ):
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 400)

    @patch("recipes.views.search_recipes")
    def test_no_results(self, mock_search):
        mock_search.return_value = []

        response = self.client.get(
            "/api/recipes/search/", {"q": "unknown"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"recipes": []})

    @patch("recipes.views.search_recipes_by_ingredient")
    def test_ingredient_search(self, mock_search):
        mock_search.return_value = [self.meal]

        response = self.client.get(
            "/api/recipes/ingredient/", {"ingredient": "pasta"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["recipes"][0]["id"], "52777"
        )
        mock_search.assert_called_once_with("pasta")

    @patch("recipes.views.get_recipe_by_id")
    def test_recipe_details(self, mock_lookup):
        mock_lookup.return_value = self.meal

        response = self.client.get("/api/recipes/52777/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["recipe"]["name"], "Pasta Salad"
        )
        mock_lookup.assert_called_once_with(52777)

    @patch("recipes.views.get_recipe_by_id")
    def test_recipe_not_found(self, mock_lookup):
        mock_lookup.return_value = None

        response = self.client.get("/api/recipes/999999/")

        self.assertEqual(response.status_code, 404)

    def test_api_failures(self):
        cases = [
            ("search_recipes", "/api/recipes/search/?q=pasta"),
            (
                "search_recipes_by_ingredient",
                "/api/recipes/ingredient/?ingredient=pasta",
            ),
            ("get_recipe_by_id", "/api/recipes/52777/"),
        ]

        for function, url in cases:
            for error in (requests.Timeout, ValueError):
                with self.subTest(function=function, error=error):
                    with patch(
                        f"recipes.views.{function}",
                        side_effect=error("Test failure"),
                    ):
                        response = self.client.get(url)
                        self.assertEqual(response.status_code, 502)

    def test_post_requests_rejected(self):
        for url in (
            "/api/recipes/search/",
            "/api/recipes/ingredient/",
            "/api/recipes/52777/",
        ):
            with self.subTest(url=url):
                response = self.client.post(url)
                self.assertEqual(response.status_code, 405)