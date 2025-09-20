"""
Comprehensive CRUD Views for all models
This module provides generic CRUD operations for all models in the system
"""

from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Import all models
from users.models import User
from masters.models import (
    Company, Contact, Category, Product, ProductImage, ProductReview,
    Tax, ChartOfAccounts, SellerProfile, SellerProduct, SellerInvoice
)
from inventory.models import (
    Cart, Order, OrderItem, PurchaseOrder, PurchaseOrderLineItem,
    SalesOrder, SalesOrderLineItem, CustomerInvoice, CustomerInvoiceLineItem,
    StockMovement
)
from reports.models import SalesReport, ProductAnalytics

# Import serializers
from users.serializers import UserSerializer
from masters.serializers import (
    CompanySerializer, ContactSerializer, CategorySerializer, ProductSerializer,
    ProductImageSerializer, ProductReviewSerializer, TaxSerializer,
    ChartOfAccountsSerializer, SellerProfileSerializer, SellerProductSerializer,
    SellerInvoiceSerializer
)
from inventory.serializers import (
    CartSerializer, OrderSerializer, OrderItemSerializer, PurchaseOrderSerializer,
    PurchaseOrderLineItemSerializer, SalesOrderSerializer, SalesOrderLineItemSerializer,
    CustomerInvoiceSerializer, CustomerInvoiceLineItemSerializer, StockMovementSerializer
)
from reports.serializers import SalesReportSerializer, ProductAnalyticsSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class CRUDMixin:
    """Mixin for common CRUD functionality"""
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Add search functionality
        search = self.request.query_params.get('search', None)
        if search:
            if hasattr(self.model, 'name'):
                queryset = queryset.filter(name__icontains=search)
            elif hasattr(self.model, 'username'):
                queryset = queryset.filter(username__icontains=search)
            elif hasattr(self.model, 'title'):
                queryset = queryset.filter(title__icontains=search)
        
        # Add ordering
        ordering = self.request.query_params.get('ordering', None)
        if ordering:
            queryset = queryset.order_by(ordering)
        
        return queryset

# =============================================================================
# USER CRUD VIEWS
# =============================================================================

class UserListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['role', 'user_type', 'is_active', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'business_name']
    ordering_fields = ['username', 'email', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class UserRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# COMPANY CRUD VIEWS
# =============================================================================

class CompanyListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'email', 'phone', 'address']
    ordering_fields = ['name', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CompanyRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# CONTACT CRUD VIEWS
# =============================================================================

class ContactListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['contact_type', 'is_active', 'company']
    search_fields = ['name', 'email', 'phone', 'address']
    ordering_fields = ['name', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ContactRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# CATEGORY CRUD VIEWS
# =============================================================================

class CategoryListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['parent', 'is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CategoryRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# PRODUCT CRUD VIEWS
# =============================================================================

class ProductListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'subcategory', 'product_type', 'is_active', 'is_featured', 'company']
    search_fields = ['name', 'description', 'sku', 'manufacturer']
    ordering_fields = ['name', 'unit_price', 'created_at', 'updated_at', 'average_rating']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# PRODUCT IMAGE CRUD VIEWS
# =============================================================================

class ProductImageListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['product', 'is_primary']
    ordering_fields = ['created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductImageRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# PRODUCT REVIEW CRUD VIEWS
# =============================================================================

class ProductReviewListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['product', 'rating', 'is_verified']
    ordering_fields = ['created_at', 'updated_at', 'rating']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductReviewRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# TAX CRUD VIEWS
# =============================================================================

class TaxListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'rate', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaxRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# CHART OF ACCOUNTS CRUD VIEWS
# =============================================================================

class ChartOfAccountsListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = ChartOfAccounts.objects.all()
    serializer_class = ChartOfAccountsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['account_type', 'is_active', 'parent']
    search_fields = ['name', 'code', 'description']
    ordering_fields = ['name', 'code', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ChartOfAccountsRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = ChartOfAccounts.objects.all()
    serializer_class = ChartOfAccountsSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# SELLER PROFILE CRUD VIEWS
# =============================================================================

class SellerProfileListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_verified', 'is_active']
    search_fields = ['business_name', 'business_type', 'description']
    ordering_fields = ['business_name', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SellerProfileRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# SELLER PRODUCT CRUD VIEWS
# =============================================================================

class SellerProductListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = SellerProduct.objects.all()
    serializer_class = SellerProductSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['seller', 'product', 'is_approved', 'is_active']
    search_fields = ['product__name', 'product__description']
    ordering_fields = ['selling_price', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class SellerProductRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = SellerProduct.objects.all()
    serializer_class = SellerProductSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# SELLER INVOICE CRUD VIEWS
# =============================================================================

class SellerInvoiceListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = SellerInvoice.objects.all()
    serializer_class = SellerInvoiceSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['seller', 'status', 'is_active']
    search_fields = ['invoice_number', 'seller__username']
    ordering_fields = ['invoice_number', 'total_sales', 'created_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class SellerInvoiceRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = SellerInvoice.objects.all()
    serializer_class = SellerInvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# CART CRUD VIEWS
# =============================================================================

class CartListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user', 'product']
    ordering_fields = ['created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

# =============================================================================
# ORDER CRUD VIEWS
# =============================================================================

class OrderListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user', 'status', 'payment_status']
    search_fields = ['order_number', 'shipping_address']
    ordering_fields = ['order_number', 'total_amount', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

# =============================================================================
# ORDER ITEM CRUD VIEWS
# =============================================================================

class OrderItemListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['order', 'product']
    ordering_fields = ['created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class OrderItemRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# PURCHASE ORDER CRUD VIEWS
# =============================================================================

class PurchaseOrderListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['supplier', 'status', 'is_active']
    search_fields = ['po_number', 'supplier__name']
    ordering_fields = ['po_number', 'total_amount', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PurchaseOrderRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# SALES ORDER CRUD VIEWS
# =============================================================================

class SalesOrderListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['customer', 'status', 'is_active']
    search_fields = ['so_number', 'customer__name']
    ordering_fields = ['so_number', 'total_amount', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SalesOrderRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# CUSTOMER INVOICE CRUD VIEWS
# =============================================================================

class CustomerInvoiceListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = CustomerInvoice.objects.all()
    serializer_class = CustomerInvoiceSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['customer', 'status', 'is_active']
    search_fields = ['invoice_number', 'customer__name']
    ordering_fields = ['invoice_number', 'total_amount', 'created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CustomerInvoiceRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerInvoice.objects.all()
    serializer_class = CustomerInvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# STOCK MOVEMENT CRUD VIEWS
# =============================================================================

class StockMovementListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['product', 'movement_type', 'reference_type']
    ordering_fields = ['created_at', 'updated_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class StockMovementRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# SALES REPORT CRUD VIEWS
# =============================================================================

class SalesReportListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ['report_date', 'created_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class SalesReportRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# PRODUCT ANALYTICS CRUD VIEWS
# =============================================================================

class ProductAnalyticsListCreateView(CRUDMixin, generics.ListCreateAPIView):
    queryset = ProductAnalytics.objects.all()
    serializer_class = ProductAnalyticsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['product', 'is_active']
    ordering_fields = ['last_updated', 'created_at']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class ProductAnalyticsRetrieveUpdateDestroyView(CRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductAnalytics.objects.all()
    serializer_class = ProductAnalyticsSerializer
    permission_classes = [permissions.IsAuthenticated]

# =============================================================================
# BULK OPERATIONS
# =============================================================================

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def bulk_delete(request, model_name):
    """Bulk delete operation for any model"""
    try:
        model_map = {
            'users': User,
            'companies': Company,
            'contacts': Contact,
            'categories': Category,
            'products': Product,
            'product_images': ProductImage,
            'product_reviews': ProductReview,
            'taxes': Tax,
            'chart_of_accounts': ChartOfAccounts,
            'seller_profiles': SellerProfile,
            'seller_products': SellerProduct,
            'seller_invoices': SellerInvoice,
            'carts': Cart,
            'orders': Order,
            'order_items': OrderItem,
            'purchase_orders': PurchaseOrder,
            'sales_orders': SalesOrder,
            'customer_invoices': CustomerInvoice,
            'stock_movements': StockMovement,
            'sales_reports': SalesReport,
            'product_analytics': ProductAnalytics,
        }
        
        if model_name not in model_map:
            return Response({'error': 'Invalid model name'}, status=status.HTTP_400_BAD_REQUEST)
        
        model = model_map[model_name]
        ids = request.data.get('ids', [])
        
        if not ids:
            return Response({'error': 'No IDs provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        deleted_count, _ = model.objects.filter(id__in=ids).delete()
        
        return Response({
            'message': f'Successfully deleted {deleted_count} records',
            'deleted_count': deleted_count
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def bulk_update(request, model_name):
    """Bulk update operation for any model"""
    try:
        model_map = {
            'users': User,
            'companies': Company,
            'contacts': Contact,
            'categories': Category,
            'products': Product,
            'product_images': ProductImage,
            'product_reviews': ProductReview,
            'taxes': Tax,
            'chart_of_accounts': ChartOfAccounts,
            'seller_profiles': SellerProfile,
            'seller_products': SellerProduct,
            'seller_invoices': SellerInvoice,
            'carts': Cart,
            'orders': Order,
            'order_items': OrderItem,
            'purchase_orders': PurchaseOrder,
            'sales_orders': SalesOrder,
            'customer_invoices': CustomerInvoice,
            'stock_movements': StockMovement,
            'sales_reports': SalesReport,
            'product_analytics': ProductAnalytics,
        }
        
        if model_name not in model_map:
            return Response({'error': 'Invalid model name'}, status=status.HTTP_400_BAD_REQUEST)
        
        model = model_map[model_name]
        ids = request.data.get('ids', [])
        update_data = request.data.get('update_data', {})
        
        if not ids or not update_data:
            return Response({'error': 'No IDs or update data provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        updated_count = model.objects.filter(id__in=ids).update(**update_data)
        
        return Response({
            'message': f'Successfully updated {updated_count} records',
            'updated_count': updated_count
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
