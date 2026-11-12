from django.contrib import admin
from django.urls import path
#from backend.groceries.views import default
#from backend.mealplans.views import default
from backend.users.views import (
    home_page,
    profile_page,
    planner_page,
)
from backend.recipes.views import (
    recipe_search,
    recipe_ingredient_search,
    recipe_detail,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/recipes/search/", recipe_search, name="recipe_search"),
    path(
        "api/recipes/ingredient/",
        recipe_ingredient_search,
        name="recipe_ingredient_search",
    ),
    path(
        "api/recipes/<int:recipe_id>/",
        recipe_detail,
        name="recipe_detail",
    ),
    path("home-page/", home_page, name = 'home'),
    path("home.html/planner.html/", planner_page),
    path("profile-page/", profile_page),
] 