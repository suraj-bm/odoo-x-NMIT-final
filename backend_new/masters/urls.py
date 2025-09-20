from django.urls import path
from . import views

urlpatterns = [
    # Company URLs
    path('companies/', views.CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', views.CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),
    
    # Contact URLs
    path('contacts/', views.ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', views.ContactRetrieveUpdateDestroyView.as_view(), name='contact-detail'),
    
    # Product URLs
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    
    # Tax URLs
    path('taxes/', views.TaxListCreateView.as_view(), name='tax-list-create'),
    path('taxes/<int:pk>/', views.TaxRetrieveUpdateDestroyView.as_view(), name='tax-detail'),
    
    # Chart of Accounts URLs
    path('chart-of-accounts/', views.ChartOfAccountsListCreateView.as_view(), name='chart-of-accounts-list-create'),
    path('chart-of-accounts/<int:pk>/', views.ChartOfAccountsRetrieveUpdateDestroyView.as_view(), name='chart-of-accounts-detail'),
]
