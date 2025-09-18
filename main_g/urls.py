from django.urls import path
from . import views

urlpatterns = [
    path("inventory/", views.InventoryListView.as_view(), name="inventory"),
    path("inventory/create/", views.CreateInventoryView.as_view(), name="create"),
    path("inventory/<int:pk>/delete/", views.DeleteInventoryView.as_view(), name="delete"),
    path("sales/new/", views.CreateSalesView.as_view(), name="sale_create"),
    path("sales/", views.SalesListView.as_view(), name="sales_list"),
    path('export/<str:period>/', views.export_sales, name='export_sales'),

]