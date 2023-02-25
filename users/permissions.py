from rest_framework import permissions
from recipes.models import Recipe


class IsUserIdOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): 
        category = Recipe.objects.filter(
            id=obj.id
        ).first()
        print(category.user.id)
        if obj.id == request.user.id:
            return True
        if category.user.id == request.user.id:
            return True

        return (
          request.user.is_authenticated
          and request.user.is_superuser
        )
