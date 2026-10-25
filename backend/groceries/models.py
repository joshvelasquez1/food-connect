from django.db import models
from django.conf import settings
from recipes.models import Ingredient

# Create your models here.
class GroceryList(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = "grocery_lists"
    )

    name = models.CharField(max_length = 150)

    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.name} for {self.user.username}"


class GroceryListItem(models.Model):

    grocery_list = models.ForeignKey(GroceryList, on_delete = models.CASCADE, related_name = "items")

    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE, related_name = "grocery_list_items")

    quantity = models.DecimalField(max_digits = 8, decimal_places = 2)
    
    unit = models.CharField(max_length = 50, blank = True, null = True)

    purchased = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.ingredient.name} ({self.quantity}) for {self.grocery_list.name}"
