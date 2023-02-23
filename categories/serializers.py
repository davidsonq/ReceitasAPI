from rest_framework import serializers
from .models import Category
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'id']
        read_only_fields = ['id']
        extra_kwargs = {
            'name' : {
                'required': True,
                'validators': [UniqueValidator(queryset=Category.objects.all(), message='A category with that username already exists.')]
            }
        }
        def create(self, validated_data):
            return Category.objects.create(**validated_data)
