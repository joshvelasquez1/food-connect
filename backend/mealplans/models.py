from django.db import models
from django.conf import settings
from recipes.models import Recipe
# Create your models here.
class MealPlan(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = "mealplans"
    )

    week_start = models.DateField()

    def __str__(self):
        return f"Meal Plan for {self.user.username} starting {self.week_start}"

class MealPlanEntry(models.Model):

    MEAL_TYPES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
    ]

    meal_type = models.CharField(max_length = 20, choices = MEAL_TYPES)

    meal_plan = models.ForeignKey(MealPlan, on_delete = models.CASCADE, related_name = "entries")

    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)

    date = models.DateField()

    def __str__(self):
        return f"{self.meal_type.capitalize()} on {self.date} for {self.meal_plan}"