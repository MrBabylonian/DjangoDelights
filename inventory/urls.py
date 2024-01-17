from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    
    path("menu/", views.MenuListView.as_view(), name="menu"),
    path("menu/add_an_item/", views.AddMenuItemView.as_view(), name="add_an_item"),
    path("menu/update_menu_item/<str:pk>/", views.UpdateMenuItemView.as_view(), name="update_menu_item"),
    
    
    path("inventory/", views.InventoryListView.as_view(), name="inventory"),
    path("inventory/add_new_product/", views.AddNewProductView.as_view(), name="add_new_product"),
    path("inventory/update_product/<pk>/", views.UpdateInventoryView.as_view(), name="update_product"),
    path("inventory/add_stock",  views.AddStockToInventoryView, name="add_stock"),
    
    
    path("recipe_list/", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipe_list/add_recipe_requirement/", views.AddRecipeRequirementView.as_view(), name="add_recipe_requirement"),
]
