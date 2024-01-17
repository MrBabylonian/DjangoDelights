from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.

class HomeView(TemplateView):
    template_name = "inventory/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MenuItemModel.objects.all()
        context["ingredient"] = IngredientModel.objects.all 
        return context




class MenuListView(ListView):
    template_name = "inventory/menu.html"
    model = MenuItemModel
    context_object_name = "menu_items"
    
class AddMenuItemView(CreateView):
    template_name = "inventory/add_menu_item.html"
    model = MenuItemModel
    form_class = MenuItemForm
    success_url = "/menu/"
    
class UpdateMenuItemView(UpdateView):
    template_name = "inventory/update_menu_item.html"
    model = MenuItemModel
    form_class = MenuItemForm
    success_url = "/menu/"
    
    

    
class InventoryListView(ListView):
    template_name = "inventory/inventory.html"
    model = IngredientModel
    
class AddNewProductView(CreateView):
    model = IngredientModel
    form_class = InventoryForm
    template_name = "inventory/add_new_product.html"
    success_url = "/inventory/"
    
class UpdateInventoryView(UpdateView):
    model = IngredientModel
    form_class = InventoryForm
    template_name = "inventory/update_inventory_item.html"
    success_url = "/inventory/"    
    
    
    
    
class RecipeListView(TemplateView):
    template_name = "inventory/recipe_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MenuItemModel.objects.all()
        context["recipe"] = RecipeRequirementModel.objects.all()
        return context
    
class AddRecipeRequirementView(CreateView):
    model = RecipeRequirementModel
    form_class = RecipeRequirementForm
    template_name = "inventory/add_recipe_requirement.html"
    success_url = '/recipe_list/'
    
class UpdateRecipeRequirementView(UpdateView):
    model = RecipeRequirementModel
    form_class = RecipeRequirementForm
    template_name = "inventory/update_recipe_requirement.html"
    
