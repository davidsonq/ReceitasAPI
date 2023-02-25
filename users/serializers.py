from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'avatar_url', 'is_superuser']
        read_only_fields = ['id', 'is_superuser']
        extra_kwargs = {
            'username': {
                'required':True,
                'validators': [UniqueValidator(queryset=User.objects.all(), message='A user with that username already exists.')]
            },
            'email': {
                'required':True,
                'validators': [UniqueValidator(queryset=User.objects.all(),)]
            },
            'password': {
                'required':True,
                'write_only': True
            }
        }    
    def create(self, validated_data):
         return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()
        return instance    


