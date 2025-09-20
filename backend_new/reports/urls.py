from django.urls import path
from . import views

urlpatterns = [
    path('stock/', views.stock_report, name='stock-report'),
    path('pnl/', views.profit_loss_report, name='profit-loss-report'),
    path('dashboard/', views.dashboard_summary, name='dashboard-summary'),
    path('ecommerce/', views.ecommerce_analytics, name='ecommerce-analytics'),
    path('product-performance/', views.product_performance, name='product-performance'),
]
