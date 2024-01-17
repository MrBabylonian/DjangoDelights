from django.db import models

# Create your models here.

class IngredientModel(models.Model):
    
    "Model for the ingredients in the stock"
    
    name = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=50)
    available_stock = models.FloatField(default=0)
    price_per_unit = models.FloatField(default=0)
    
    class Meta:
        
        ordering = ['-price_per_unit']
        verbose_name = "Ingredient"
        
    def __str__(self):
        return self.name
    
    def full_price(self):
        return f"{self.price_per_unit} €"
    
    def stock_unit(self):
        return f"{self.available_stock} {self.unit}"
    
    
class MenuItemModel(models.Model):
    
    "Model for the menu items"
    
    name = models.CharField(max_length=50, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.ManyToManyField(IngredientModel, blank=True)
    
    class Meta:
        
        verbose_name = "Menu Item"
        ordering = ['-price']
    
    def __str__(self):
        return self.name
    
    def full_price(self):
        return f"{self.price} €"
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
    
    
class RecipeRequirementModel(models.Model):
    
    "Model for the recipe requirements of the menu items"
    
    menu_item = models.ForeignKey(MenuItemModel, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(IngredientModel, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    
    class Meta:
        
        verbose_name = "Recipe Requirement"
        
    def __str__(self):
        return f"Menu Item : {self.menu_item.__str__} Ingredients : {self.ingredients.name} Quantity : {self.quantity}"
    
    def recipe(self):
        return f"{self.ingredients.name} : {self.quantity} {self.ingredients.unit}"
    
class PurchaseModel(models.Model):
    
    "Model to keep track of the sales"
    
    menu_item = models.ForeignKey(MenuItemModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        
        verbose_name = "Sale"