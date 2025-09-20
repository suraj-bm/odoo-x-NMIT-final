from django.urls import path
from . import views

urlpatterns = [
    # Purchase Order URLs
    path('purchase-orders/', views.PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase-orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-detail'),
    path('purchase-orders/<int:po_id>/convert-to-bill/', views.convert_po_to_bill, name='convert-po-to-bill'),
    
    # Sales Order URLs
    path('sales-orders/', views.SalesOrderListCreateView.as_view(), name='sales-order-list-create'),
    path('sales-orders/<int:pk>/', views.SalesOrderRetrieveUpdateDestroyView.as_view(), name='sales-order-detail'),
    path('sales-orders/<int:so_id>/convert-to-invoice/', views.convert_so_to_invoice, name='convert-so-to-invoice'),
    
    # Vendor Bill URLs
    path('bills/', views.VendorBillListCreateView.as_view(), name='vendor-bill-list-create'),
    path('bills/<int:pk>/', views.VendorBillRetrieveUpdateDestroyView.as_view(), name='vendor-bill-detail'),
    
    # Customer Invoice URLs
    path('invoices/', views.CustomerInvoiceListCreateView.as_view(), name='customer-invoice-list-create'),
    path('invoices/<int:pk>/', views.CustomerInvoiceRetrieveUpdateDestroyView.as_view(), name='customer-invoice-detail'),
    
    # Stock Movement URLs
    path('stock-movements/', views.StockMovementListCreateView.as_view(), name='stock-movement-list-create'),
    
    # E-commerce URLs
    path('cart/', views.CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', views.CartRetrieveUpdateDestroyView.as_view(), name='cart-detail'),
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    path('checkout/', views.checkout, name='checkout'),
]
