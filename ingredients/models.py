from django.db import models

class Ingredient(models.Model):
    name=models.CharField(max_length=125, unique=True)
    
