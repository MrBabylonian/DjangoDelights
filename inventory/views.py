from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
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
    
    
class AddRecipeRequirement(CreateView):
    model = RecipeRequirementModel
    form_class = AddRecipeRequirementForm
    template_name = "inventory/add_recipe_requirement.html"
    success_url = '/menu/'