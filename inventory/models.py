from django.db import models

# Create your models here.

class IngredientModel(models.Model):
    "Model for the ingredients in the stock"
    
    name = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=50)
    available_stock = models.FloatField(max_length=50)
    price_per_unit = models.FloatField(max_length=10, default="€")
    
    
class MenuItemModel(models.Model):
    
    "Model for the menu items"
    
    name = models.CharField(max_length=50, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    required_ingredients = models.ManyToManyField(IngredientModel, blank=True)
    
    
class RecipeRequirementModel(models.Model):
    
    "Model for the recipe requirements of the menu items"
    
    menu_item = models.ForeignKey(MenuItemModel, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(IngredientModel, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    
    
class PurchaseModel(models.Model):
    
    "Model to keep track of the sales"
    
    menu_item = models.ForeignKey(MenuItemModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)