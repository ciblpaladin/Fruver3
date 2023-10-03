from django.urls import path
from .Views.InventoryView import ListaTareas
from .Views.ProductsView import Products

urlpatterns = [

     path('products/', ListaTareas.as_view()),
     path('products2/', Products.ProductViewList.as_view())
]
