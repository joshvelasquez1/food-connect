from django.contrib import admin
from django.urls import path
from recipes.views import recipe_search

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/recipes/search/", recipe_search, name="recipe_search"),
]