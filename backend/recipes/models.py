from django.db import models

# Create your models here.
class Ingredient(models.Model):

    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Recipe(models.Model):

    name = models.CharField(max_length = 200)

    description = models.TextField(blank = True)

    instructions = models.TextField()

    servings = models.PositiveIntegerField(default = 1)

    preparation_time = models.PositiveIntegerField(default = 0)

    ingredients = models.ManyToManyField(Ingredient, through = "RecipeIngredient")

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)

    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)

    quantity = models.DecimalField(
        max_digits = 8,
        decimal_places = 2
    )

    unit = models.CharField(max_length = 50)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["recipe", "ingredient"],
                name="unique_recipe_ingredient"
            )
        ]

