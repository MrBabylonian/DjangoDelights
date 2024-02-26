from django.shortcuts import render,  get_object_or_404, redirect
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout


# Create your views here.
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = "/sales/"
    
def LogoutView(request):
    logout(request)
    return redirect("home")




class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MenuItemModel.objects.all()
        context["ingredient"] = IngredientModel.objects.all 
        return context
    

#views regarding the Menu Items
class MenuListView(LoginRequiredMixin, ListView):
    template_name = "inventory/menu.html"
    model = MenuItemModel
    context_object_name = "menu_items"
 
class AddMenuItemView(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_menu_item.html"
    model = MenuItemModel
    form_class = MenuItemForm
    success_url = "/menu/"
    
class UpdateMenuItemView(LoginRequiredMixin, UpdateView):
    template_name = "inventory/update_menu_item.html"
    model = MenuItemModel
    form_class = MenuItemForm
    success_url = "/menu/"
    
class DeleteMenuItemView(LoginRequiredMixin, DeleteView):
    model = MenuItemModel
    template_name = "inventory/delete_menu_item.html"
    success_url = "/menu/"
    
    

#Views regarding the Ingredients&Stock    
class InventoryListView(LoginRequiredMixin, ListView):
    template_name = "inventory/inventory.html"
    model = IngredientModel
    
class AddNewProductView(LoginRequiredMixin, CreateView):
    model = IngredientModel
    form_class = InventoryForm
    template_name = "inventory/add_new_product.html"
    success_url = "/inventory/"
    
class UpdateInventoryView(LoginRequiredMixin, UpdateView):
    model = IngredientModel
    form_class = InventoryForm
    template_name = "inventory/update_inventory_item.html"
    success_url = "/inventory/"

@login_required    
def AddStockToInventoryView(request):
    if request.method == "POST":
        form = AddStockToInventoryForm(request.POST)
        if form.is_valid():
            ingredient = form.cleaned_data['ingredient']
            add_stock = form.cleaned_data['add_stock']
            ingredient.available_stock += add_stock
            ingredient.save()
            return redirect('/inventory/')
    else:
        ingredient_id = request.GET.get('ingredient_id')
        if ingredient_id:
            ingredient = get_object_or_404(IngredientModel, id=ingredient_id)
            form = AddStockToInventoryForm(initial={'ingredient' : ingredient, 'available_stock' : IngredientModel.available_stock})
        else:
            form = AddStockToInventoryForm
    return render(request, 'inventory/add_stock_to_inventory.html', {'form': form})

class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    model = IngredientModel
    template_name = "inventory/delete_ingredient.html"
    success_url= "/inventory/"           
    
    
    
#Views regarding the Recipes 
class RecipeListView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/recipe_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = MenuItemModel.objects.all()
        context["recipe"] = RecipeRequirementModel.objects.all()
        return context
    
class AddRecipeRequirementView(LoginRequiredMixin, CreateView):
    model = RecipeRequirementModel
    form_class = RecipeRequirementForm
    template_name = "inventory/add_recipe_requirement.html"
    success_url = '/recipe_list/'

class UpdateRecipeRequirementView(LoginRequiredMixin, UpdateView):
    model = RecipeRequirementModel
    form_class = UpdateRecipeRequirementForm
    template_name = "inventory/update_recipe_requirement.html"
    success_url = '/recipe_list/'
    
    
    
    
#Views regarding the sales

class SaleListView(LoginRequiredMixin, ListView):
    model = PurchaseModel
    template_name = "inventory/sale_list.html"
    context_object_name = "sales"

#Method to check if there is enough stock of required ingredients for the menu item to be sold   
def has_enough_stock(menu_item):
    for recipe_requirement in menu_item.reciperequirementmodel_set.all():
        ingredients = recipe_requirement.ingredients
        quantity_needed = recipe_requirement.quantity
        if ingredients.available_stock < quantity_needed:
            return False
    return True

@login_required    
def NewSaleView(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            menu_item = form.cleaned_data['menu_item']

            # Check if there is enough stock for the ingredients
            if has_enough_stock(menu_item):
                # Save the sale
                form.save()

                # Deduct ingredients used from stock
                for recipe_requirement in menu_item.reciperequirementmodel_set.all():
                    ingredient = recipe_requirement.ingredients
                    quantity_used = recipe_requirement.quantity
                    ingredient.available_stock -= quantity_used
                    ingredient.save()
            
                return redirect("/sales/")
            else:
                messages.error(request, 'Not enough stock for the required ingredients.')
    else:
        form = SaleForm()

    return render(request, "inventory/add_new_sale.html", {'form': form})
        
        
    
class DeleteSaleView(LoginRequiredMixin, DeleteView):
    model = PurchaseModel
    template_name = "inventory/delete_sale.html"
    success_url = '/sales/'
    