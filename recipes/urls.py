from django.urls import path
from . import views


urlpatterns = [
    path("recipes/", views.CreateRecipeView.as_view()),
    path("recipes/<uuid:pk>/", views.RecipeDetailView.as_view()),
]
