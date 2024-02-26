from django.db import models
from django.db.models import Sum, F

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
    
    #Sub-method to display the full price of an ingredient
    def full_price(self):
        return f"{self.price_per_unit} €"
        
    #Sub-method to display the available stock of an ingredient
    def stock_unit(self):
        return f"{round(self.available_stock, 2)} {self.unit}"
            
    
    
    
class MenuItemModel(models.Model):
    
    "Model for the menu items"
    
    name = models.CharField(max_length=50, primary_key=True)
    price = models.FloatField()
    ingredients = models.ManyToManyField(IngredientModel, blank=True)
    
    class Meta:
        
        verbose_name = "Menu Item"
        ordering = ['-price']
    
    
    def __str__(self):
        return self.name
    
    #Sub-method to display the full price of a menu item
    def full_price(self):
        return f"{self.price} €"
    
    #Sub-method to calculate the production cost of a menu item using the "cost_per_ingredient" sub-method
    #from the "RecipeRequirementModel"
    def production_cost_per_menu_item(self):
        total_cost = 0
        for recipe_requirement in self.reciperequirementmodel_set.all():
            total_cost += recipe_requirement.cost_per_ingredient()
        return round(total_cost, 3)
    
    #Sub-method to calculate the profit per menu item
    def profit_per_menu_item(self):
        profit = self.price - self.production_cost_per_menu_item()
        return round(profit, 2)
        
        
    
                   
    
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
        return f"Menu Item : {self.menu_item.name} Ingredients : {self.ingredients.name} Quantity : {self.quantity} { self.ingredients.unit }"
    
    #Sub-method to display a recipe requirement for a given menu item
    def recipe(self):
        return f"{self.ingredients.name} : {self.quantity} {self.ingredients.unit}"
    
    
    #Sub-method to calculate the cost of an ingredient for a given menu item according to the quantity used
    #This method is also used to calculate the production cost of a menu item
    def cost_per_ingredient(self):
        cost_per_ingredient = self.quantity * self.ingredients.price_per_unit
        return round(cost_per_ingredient, 2)

    
class PurchaseModel(models.Model):
    
    "Model to keep track of the sales"
    
    menu_item = models.ForeignKey(MenuItemModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        
        verbose_name = "Sale"
        ordering = ["-timestamp"]
        
    def __str__(self):
        return f"{ self.menu_item } Day: {self.timestamp.date()} Time: {self.timestamp.time()}"
    
    #Sub-method to calculate and display the amount of total sale made so far
    def total_revenue(self):
        total_revenue = PurchaseModel.objects.aggregate(total_revenue=Sum(F('menu_item__price')))['total_revenue']
        return round(total_revenue, 2)
    
    def total_profit(self):
        total_profit = 0
        for sale in PurchaseModel.objects.all():
            profit = sale.menu_item.price - sale.menu_item.production_cost_per_menu_item()
            total_profit += profit
        return round(total_profit, 2)
    
    def total_cost(self):
        total_revenue = self.total_revenue()
        total_profit = self.total_profit()
        total_cost = total_revenue - total_profit
        return round(total_cost, 2)
                
                
            
    
    

         