from rest_framework import serializers
from .models import Recipe
from categories.serializers import CategorySerializer
from categories.models import Category
from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer


class RecipeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    ingredients = IngredientSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ['user']
        depth = 1

    def create(self, validated_data):
        category_value = validated_data.pop('category')
        ingredient_value = validated_data.pop('ingredients')
        category = Category.objects.filter(
            name__iexact=category_value["name"]
        ).first()
        if not category:
            category = Category.objects.create(**category_value)
        recipe = Recipe.objects.create(category=category, **validated_data)
        for ingredient in ingredient_value:
            new_ingredient = Ingredient.objects.filter(
                    name__iexact=ingredient["name"]
            ).first()
            if not new_ingredient:
                new_ingredient = Ingredient.objects.create(
                    name=ingredient["name"]
                )
            recipe.ingredients.add(new_ingredient)

        return recipe

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            
            if attr == 'category':
                category = Category.objects.filter(
                    name__iexact=value["name"]
                ).first()
                if not category:
                    category = Category.objects.create(**value)
                setattr(instance, attr, category)
            elif attr == "ingredients":
                instance.ingredients.clear()
                for ingredient in value:
                    new_ingredient = Ingredient.objects.filter(
                        name__iexact=ingredient["name"]
                    ).first()
                    if not new_ingredient:
                        new_ingredient = Ingredient.objects.create(
                            name=ingredient["name"]
                        )
                    instance.ingredients.add(new_ingredient)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance