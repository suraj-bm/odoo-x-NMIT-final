"""
Comprehensive URL patterns for all CRUD operations
"""

from django.urls import path, include
import crud_views

# =============================================================================
# USER CRUD URLS
# =============================================================================
user_urls = [
    path('', crud_views.UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', crud_views.UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]

# =============================================================================
# COMPANY CRUD URLS
# =============================================================================
company_urls = [
    path('', crud_views.CompanyListCreateView.as_view(), name='company-list-create'),
    path('<int:pk>/', crud_views.CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),
]

# =============================================================================
# CONTACT CRUD URLS
# =============================================================================
contact_urls = [
    path('', crud_views.ContactListCreateView.as_view(), name='contact-list-create'),
    path('<int:pk>/', crud_views.ContactRetrieveUpdateDestroyView.as_view(), name='contact-detail'),
]

# =============================================================================
# CATEGORY CRUD URLS
# =============================================================================
category_urls = [
    path('', crud_views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('<int:pk>/', crud_views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
]

# =============================================================================
# PRODUCT CRUD URLS
# =============================================================================
product_urls = [
    path('', crud_views.ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', crud_views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('<int:product_id>/images/', crud_views.ProductImageListCreateView.as_view(), name='product-image-list-create'),
    path('<int:product_id>/images/<int:pk>/', crud_views.ProductImageRetrieveUpdateDestroyView.as_view(), name='product-image-detail'),
    path('<int:product_id>/reviews/', crud_views.ProductReviewListCreateView.as_view(), name='product-review-list-create'),
    path('<int:product_id>/reviews/<int:pk>/', crud_views.ProductReviewRetrieveUpdateDestroyView.as_view(), name='product-review-detail'),
]

# =============================================================================
# TAX CRUD URLS
# =============================================================================
tax_urls = [
    path('', crud_views.TaxListCreateView.as_view(), name='tax-list-create'),
    path('<int:pk>/', crud_views.TaxRetrieveUpdateDestroyView.as_view(), name='tax-detail'),
]

# =============================================================================
# CHART OF ACCOUNTS CRUD URLS
# =============================================================================
chart_of_accounts_urls = [
    path('', crud_views.ChartOfAccountsListCreateView.as_view(), name='chart-of-accounts-list-create'),
    path('<int:pk>/', crud_views.ChartOfAccountsRetrieveUpdateDestroyView.as_view(), name='chart-of-accounts-detail'),
]

# =============================================================================
# SELLER CRUD URLS
# =============================================================================
seller_urls = [
    path('seller-profiles/', crud_views.SellerProfileListCreateView.as_view(), name='seller-profile-list-create'),
    path('seller-profiles/<int:pk>/', crud_views.SellerProfileRetrieveUpdateDestroyView.as_view(), name='seller-profile-detail'),
    path('seller-products/', crud_views.SellerProductListCreateView.as_view(), name='seller-product-list-create'),
    path('seller-products/<int:pk>/', crud_views.SellerProductRetrieveUpdateDestroyView.as_view(), name='seller-product-detail'),
    path('seller-invoices/', crud_views.SellerInvoiceListCreateView.as_view(), name='seller-invoice-list-create'),
    path('seller-invoices/<int:pk>/', crud_views.SellerInvoiceRetrieveUpdateDestroyView.as_view(), name='seller-invoice-detail'),
]

# =============================================================================
# E-COMMERCE CRUD URLS
# =============================================================================
ecommerce_urls = [
    path('carts/', crud_views.CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', crud_views.CartRetrieveUpdateDestroyView.as_view(), name='cart-detail'),
    path('orders/', crud_views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', crud_views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    path('order-items/', crud_views.OrderItemListCreateView.as_view(), name='order-item-list-create'),
    path('order-items/<int:pk>/', crud_views.OrderItemRetrieveUpdateDestroyView.as_view(), name='order-item-detail'),
]

# =============================================================================
# PURCHASE CRUD URLS
# =============================================================================
purchase_urls = [
    path('purchase-orders/', crud_views.PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase-orders/<int:pk>/', crud_views.PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-detail'),
]

# =============================================================================
# SALES CRUD URLS
# =============================================================================
sales_urls = [
    path('sales-orders/', crud_views.SalesOrderListCreateView.as_view(), name='sales-order-list-create'),
    path('sales-orders/<int:pk>/', crud_views.SalesOrderRetrieveUpdateDestroyView.as_view(), name='sales-order-detail'),
    path('customer-invoices/', crud_views.CustomerInvoiceListCreateView.as_view(), name='customer-invoice-list-create'),
    path('customer-invoices/<int:pk>/', crud_views.CustomerInvoiceRetrieveUpdateDestroyView.as_view(), name='customer-invoice-detail'),
]

# =============================================================================
# INVENTORY CRUD URLS
# =============================================================================
inventory_urls = [
    path('stock-movements/', crud_views.StockMovementListCreateView.as_view(), name='stock-movement-list-create'),
    path('stock-movements/<int:pk>/', crud_views.StockMovementRetrieveUpdateDestroyView.as_view(), name='stock-movement-detail'),
]

# =============================================================================
# REPORTS CRUD URLS
# =============================================================================
reports_urls = [
    path('sales-reports/', crud_views.SalesReportListCreateView.as_view(), name='sales-report-list-create'),
    path('sales-reports/<int:pk>/', crud_views.SalesReportRetrieveUpdateDestroyView.as_view(), name='sales-report-detail'),
    path('product-analytics/', crud_views.ProductAnalyticsListCreateView.as_view(), name='product-analytics-list-create'),
    path('product-analytics/<int:pk>/', crud_views.ProductAnalyticsRetrieveUpdateDestroyView.as_view(), name='product-analytics-detail'),
]

# =============================================================================
# BULK OPERATIONS URLS
# =============================================================================
bulk_urls = [
    path('bulk/delete/<str:model_name>/', crud_views.bulk_delete, name='bulk-delete'),
    path('bulk/update/<str:model_name>/', crud_views.bulk_update, name='bulk-update'),
]

# =============================================================================
# MAIN URL PATTERNS
# =============================================================================
urlpatterns = [
    # User Management
    path('users/', include(user_urls)),
    
    # Master Data
    path('companies/', include(company_urls)),
    path('contacts/', include(contact_urls)),
    path('categories/', include(category_urls)),
    path('products/', include(product_urls)),
    path('taxes/', include(tax_urls)),
    path('chart-of-accounts/', include(chart_of_accounts_urls)),
    
    # Seller Management
    path('sellers/', include(seller_urls)),
    
    # E-commerce
    path('ecommerce/', include(ecommerce_urls)),
    
    # Purchase Management
    path('purchases/', include(purchase_urls)),
    
    # Sales Management
    path('sales/', include(sales_urls)),
    
    # Inventory Management
    path('inventory/', include(inventory_urls)),
    
    # Reports & Analytics
    path('reports/', include(reports_urls)),
    
    # Bulk Operations
    path('bulk/', include(bulk_urls)),
]
