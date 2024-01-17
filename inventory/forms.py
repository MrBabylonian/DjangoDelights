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

class AddStockToInventoryForm(forms.ModelForm):
    class Meta:
        model = IngredientModel
        fields = ['available_stock']
    
    ingredient = forms.ModelChoiceField(queryset=IngredientModel.objects.all())
    add_stock = forms.FloatField(min_value = 0)
    available_stock = forms.FloatField(widget=forms.HiddenInput(), required=False)
    