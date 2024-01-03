from django.urls import path
from .Views.ProductsView import Products
from .Views.InventoryView import Inventory
from .Views.SuppliersView import Suppliers, SuppliersDebts
from .Views.DebtorsView import Debtors, DebtorsCredits
from .Views.UserView import User
from .Views.RecordsView import Records
from rest_framework.authtoken import views

urlpatterns = [


     ##Productos end points=====================================================
     path('get_token/', views.obtain_auth_token),

     path('users_create/', User.UserCreateList.as_view()),

     path('products/', Products.ProductViewList.as_view()),
     path('products_create', Products.ProductViewList.as_view()),
     path('products_update', Products.ProductCreateList.as_view()),
     path('products_filter', Products.ProductfilterView.as_view()),
     ##Inventarios end points==================================================
     
     path('Inventorybox/', Inventory.InventoryBoxListDate.as_view()),
     path('Inventorybox_create', Inventory.InvetoryBoxList.as_view()),
     path('Inventorybox_check_date', Inventory.InventoryDateCheckView.as_view()),
     path('Inventorybox_update', Inventory.InventoryUpdateView.as_view()),

     path('Inventoryunit/', Inventory.InvetoryUnitListDate.as_view()),
     path('Inventoryunit_create', Inventory.InvetoryUnitList.as_view()),
     path('Inventoryunit_check_date', Inventory.InventoryUnitDateCheckView.as_view()),
     path('Inventoryunit_update', Inventory.InventoryUnitUpdateView.as_view()),

     ## proveedores end points=================================================
    
     path('suppliers/', Suppliers.SuppliersViewList.as_view()),
     path('suppliers_create', Suppliers.SuppliersViewList.as_view()),
     path('suppliers_filter', Suppliers.SuppliersFilterView.as_view()),
     path('suppliers_update', Suppliers.SuppliersUpdateView.as_view()),


     path('suppliersdebts/', SuppliersDebts.SuppliersDebtsViewList.as_view()),
     path('suppliersdebts_create', SuppliersDebts.SuppliersDebtsViewList.as_view()),
     path('suppliersdebts_filter', SuppliersDebts.SuppliersDebtsFilterView.as_view()),
     path('suppliers_debts_paid_off', SuppliersDebts.SuppliersDebtsPayView.as_view()),
     path('suppliers_debts_pass', SuppliersDebts.SuppliersDebtsPassView.as_view()),
     path('suppliers_debts_paids/', SuppliersDebts.SuppliersDebtsPayView.as_view()),
     path('suppliers_debts_paids_filter', SuppliersDebts.SuppliersDebtsPayFilterView.as_view()),
     #HISTORIAL DE DEUDAS
     path('suppliers_debts_history/', SuppliersDebts.SuppliersDebtsHistoryView.as_view()),
     path('suppliers_debts_total/', SuppliersDebts.SuppliersDebtsTotalView.as_view()), #total
     ## deudores end points=====================================================

     path('debtors/', Debtors.DebtorsViewList.as_view()),
     path('debtors_create', Debtors.DebtorsViewList.as_view()),
     path('debtors_edit', Debtors.DebtorsDetailsView.as_view()),
     path('debtors_update/', Debtors.DebtorsUpdateView.as_view()),
     path('debtors_filter/', Debtors.DebtorsFilterView.as_view()),

     path('debtorscredits/', DebtorsCredits.DebtorsCreditsViewList.as_view()),
     path('debtorscredits_pays/', DebtorsCredits.CreditPaysView.as_view()),
     path('debtorscredits_payoff_credit/', DebtorsCredits.CreditPayOfCreditView.as_view()),
     path('debtorscredits_create/', DebtorsCredits.DebtorsCreditsViewList.as_view()),
     path('debtorscredits_edit/', DebtorsCredits.DebtorsCreditsViewEdit.as_view()),
     path('debtorscredits_filter/', DebtorsCredits.DebtorsCreditsViewFilter.as_view()),
     path('debtorscredits_paids_filter/', DebtorsCredits.CreditPaysView.as_view()),

     
     path('debtorscredits_total', DebtorsCredits.CreditTotalView.as_view()), #total
     

     #HISTORIAL DE CREDITO
     path('debtorscredits_credit_history/', DebtorsCredits.CreditHistoryView.as_view()),
     path('debtorscredits_filter_history/', DebtorsCredits.CreditHistoryView.as_view()),

     ##URL PARA ELIMINAR REGISTROS 
     path('records/delete_soft', Records.RecordsViewList.as_view()),

     ##URL PARA filtrar tablas por solo 1 campo 
     path('records/filter', Records.RecordsFilterView.as_view())
     
]
