from rest_framework import serializers
from .models import Recipe
from categories.models import Category
from ingredients.models import Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        
    
    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        category_name = validated_data.pop('category')
        category, _ = Category.objects.get_or_create(name__exact=category_name)

        recipe = Recipe.objects.create(
            category=category,
            **validated_data
        )

        for ingredient_name in ingredients_data:
            ingredient, _ = Ingredient.objects.get_or_create(name__exact=ingredient_name)
            recipe.ingredients.add(ingredient)

        return recipe

    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'ingredients':
                instance.ingredients.clear()
                for ingredient_name in value:
                    ingredient, _ = Ingredient.objects.get_or_create(name__exact=ingredient_name)
                    instance.ingredients.add(ingredient)
            elif key == 'category':
                category_name = value
                category, _ = Category.objects.get_or_create(name__exact=category_name)
                instance.category = category
            else:
                setattr(instance, key, value)

        instance.save()
        return instance    