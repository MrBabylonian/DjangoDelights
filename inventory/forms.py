from django import forms
from .models import *

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirementModel
        fields = "__all__"
        

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItemModel
        fields = "__all__"
        

class InventoryForm(forms.ModelForm):
    class Meta:
        model = IngredientModel
        fields = ['name', 'unit', 'price_per_unit']
