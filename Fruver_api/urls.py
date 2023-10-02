from django.urls import path
from .Views.InventoryView import ListaTareas

urlpatterns = [

     path('usuarios/', ListaTareas.as_view())
]
