from django.db import models
from ingredients.models import Ingredient 

class Recipe(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField()
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.PROTECT
    )
    ingredients = models.ManyToManyField(Ingredient)

