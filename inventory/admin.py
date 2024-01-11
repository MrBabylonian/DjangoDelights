from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(IngredientModel)
admin.site.register(MenuItemModel)
admin.site.register(RecipeRequirementModel)
admin.site.register(PurchaseModel)
