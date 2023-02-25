from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.CreateUserView.as_view()),
    path("users/<uuid:pk>/", views.UserDetailView.as_view()),
    path("users/profile/", views.ProfileView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
