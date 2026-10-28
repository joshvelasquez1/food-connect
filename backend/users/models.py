from django.db import models
from django.conf import settings


# Create your models here.

class UserPreferences(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = "preferences"
    )

    dietary_restrictions = models.JSONField(default = list, blank = True)

    allergies = models.JSONField(default = list, blank = True)

    weekly_model = models.DecimalField(
        max_digits = 8,
        decimal_places = 2,
        default = 0
    )

    def __str__(self):
        return f"{self.user.username}'s preferences"

