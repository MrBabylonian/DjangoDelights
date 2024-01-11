from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = "inventory/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MenuItemModel.objects.all()
        context["ingredient"] = IngredientModel.objects.all 
        return context
    