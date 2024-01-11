from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("menu/", views.MenuListView.as_view(), name="menu"),
    path("add_recipe_requirement/", views.AddRecipeRequirement.as_view(), name="add_recipe_requirement")
]
