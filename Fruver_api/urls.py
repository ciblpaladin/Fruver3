from django.urls import path
from .Views.InventoryView import ListaTareas

urlpatterns = [

     path('products/', ListaTareas.as_view())
]
