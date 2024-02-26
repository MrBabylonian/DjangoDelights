from django import forms
from .models import *
from .views import *

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirementModel
        fields = "__all__"
        
class UpdateRecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirementModel
        fields = ['quantity']



class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItemModel
        fields = "__all__"
        



class InventoryForm(forms.ModelForm):
    class Meta:
        model = IngredientModel
        fields = ['name', 'unit', 'price_per_unit']

class AddStockToInventoryForm(forms.ModelForm):
    class Meta:
        model = IngredientModel
        fields = ['available_stock']
    
    ingredient = forms.ModelChoiceField(queryset=IngredientModel.objects.all())
    add_stock = forms.FloatField(min_value = 0)
    available_stock = forms.FloatField(widget=forms.HiddenInput(), required=False)
    




class SaleForm(forms.ModelForm):
    class Meta:
        model = PurchaseModel
        fields = ['menu_item']
        
    menu_item = forms.ModelChoiceField(queryset=MenuItemModel.objects.all())