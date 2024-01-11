from django import forms
from .models import *

class AddRecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirementModel
        fields = "__all__"
