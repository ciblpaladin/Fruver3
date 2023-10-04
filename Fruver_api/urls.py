from django.urls import path
from .Views.ProductsView import Products
from .Views.InventoryView import Inventory
from .Views.SuppliersView import Suppliers, SuppliersDebts
from .Views.DebtorsView import Debtors, DebtorsCredits

urlpatterns = [


     ##Productos end points=====================================================
     
     path('products/', Products.ProductViewList.as_view()),
     path('products_create', Products.ProductViewList.as_view()),
     ##Inventarios end points==================================================
     
     path('Inventorybox/', Inventory.InvetoryBoxList.as_view()),
     path('Inventoryunit/', Inventory.InvetoryUnitList.as_view()),

     ## proveedores end points=================================================
    
     path('suppliers/', Suppliers.SuppliersViewList.as_view()),
     path('suppliers_create', Suppliers.SuppliersViewList.as_view()),

     path('suppliersdebts/', SuppliersDebts.SuppliersDebtsViewList.as_view()),

     ## deudores end points=====================================================

     path('debtors/', Debtors.DebtorsViewList.as_view()),
     path('debtors_create', Debtors.DebtorsViewList.as_view()),

     path('debtorscredits/', DebtorsCredits.DebtorsCreditsViewList.as_view()),
     path('debtorscredits_create', DebtorsCredits.DebtorsCreditsViewList.as_view()),
]
