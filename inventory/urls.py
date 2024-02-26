from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls"), name="login"),
    path("logout/", views.LogoutView, name="logout"),
    
    #Menu
    path("menu/", views.MenuListView.as_view(), name="menu"),
    path("menu/add_an_item/", views.AddMenuItemView.as_view(), name="add_an_item"),
    path("menu/update_menu_item/<str:pk>/", views.UpdateMenuItemView.as_view(), name="update_menu_item"),
    path("menu/<str:pk>/delete_menu_item/", views.DeleteMenuItemView.as_view(), name="delete_menu_item"),
    
    #Inventory&Ingredients
    path("inventory/", views.InventoryListView.as_view(), name="inventory"),
    path("inventory/add_new_product/", views.AddNewProductView.as_view(), name="add_new_product"),
    path("inventory/update_product/<pk>/", views.UpdateInventoryView.as_view(), name="update_product"),
    path("inventory/add_stock",  views.AddStockToInventoryView, name="add_stock"),
    path("inventory/<pk>/delete_ingredient", views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    
    #Recipe
    path("recipe_list/", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipe_list/add_recipe_requirement/", views.AddRecipeRequirementView.as_view(), name="add_recipe_requirement"),
    path("recipe_list/<pk>/update_recipe_requirement/", views.UpdateRecipeRequirementView.as_view(), name="update_recipe_requirement"),
    
    #Sales
    path("sales/", views.SaleListView.as_view(), name="sale_list"),
    path("sales/new_sale", views.NewSaleView, name="new_sale"),
    path("sales/<pk>/delete_sale/", views.DeleteSaleView.as_view(), name="delete_sale"),
]
