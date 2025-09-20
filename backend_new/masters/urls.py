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
    
    # Category URLs
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    
    # Product Review URLs
    path('products/<int:product_id>/reviews/', views.ProductReviewListCreateView.as_view(), name='product-review-list-create'),
    
    # Product Image URLs
    path('products/<int:product_id>/images/', views.ProductImageListCreateView.as_view(), name='product-image-list-create'),
    
    # Seller Profile URLs
    path('seller-profiles/', views.SellerProfileListCreateView.as_view(), name='seller-profile-list-create'),
    path('seller-profiles/<int:pk>/', views.SellerProfileRetrieveUpdateDestroyView.as_view(), name='seller-profile-detail'),
    
    # Seller Product URLs
    path('seller-products/', views.SellerProductListCreateView.as_view(), name='seller-product-list-create'),
    path('seller-products/<int:pk>/', views.SellerProductRetrieveUpdateDestroyView.as_view(), name='seller-product-detail'),
    path('seller-products/<int:product_id>/approve/', views.approve_seller_product, name='approve-seller-product'),
    
    # Admin Seller Management URLs
    path('admin/seller-products/', views.AdminSellerProductListCreateView.as_view(), name='admin-seller-product-list-create'),
    path('admin/seller-products/<int:pk>/', views.AdminSellerProductRetrieveUpdateDestroyView.as_view(), name='admin-seller-product-detail'),
    
    # Seller Invoice URLs
    path('seller-invoices/', views.SellerInvoiceListCreateView.as_view(), name='seller-invoice-list-create'),
    path('seller-invoices/<int:pk>/', views.SellerInvoiceRetrieveUpdateDestroyView.as_view(), name='seller-invoice-detail'),
]
