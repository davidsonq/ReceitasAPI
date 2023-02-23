from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Ingredient





class IngredientSerialize(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']
        extra_kwargs = {
            'name' : {
                'required': True,
                'validators': [UniqueValidator(queryset=Ingredient.objects.all(), message='A ingredient with that username already exists.')]
            }
        }
        def create(self, validated_data):
            return Ingredient.objects.create(**validated_data)