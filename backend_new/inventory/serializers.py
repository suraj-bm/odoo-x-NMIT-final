from rest_framework import serializers
from .models import (
    PurchaseOrder, PurchaseOrderLineItem,
    SalesOrder, SalesOrderLineItem,
    VendorBill, VendorBillLineItem,
    CustomerInvoice, CustomerInvoiceLineItem,
    StockMovement, Cart, Order, OrderItem
)
from masters.serializers import ContactSerializer, ProductSerializer

class PurchaseOrderLineItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    
    class Meta:
        model = PurchaseOrderLineItem
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class PurchaseOrderSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    line_items = PurchaseOrderLineItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'po_number')

class SalesOrderLineItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    
    class Meta:
        model = SalesOrderLineItem
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class SalesOrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    line_items = SalesOrderLineItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = SalesOrder
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'so_number')

class VendorBillLineItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    
    class Meta:
        model = VendorBillLineItem
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class VendorBillSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    po_number = serializers.CharField(source='purchase_order.po_number', read_only=True)
    line_items = VendorBillLineItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = VendorBill
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'bill_number')

class CustomerInvoiceLineItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    
    class Meta:
        model = CustomerInvoiceLineItem
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class CustomerInvoiceSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    so_number = serializers.CharField(source='sales_order.so_number', read_only=True)
    line_items = CustomerInvoiceLineItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomerInvoice
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'invoice_number')

class StockMovementSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    
    class Meta:
        model = StockMovement
        fields = '__all__'
        read_only_fields = ('created_at',)

class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.unit_price', max_digits=12, decimal_places=2, read_only=True)
    product_image = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
    
    def get_product_image(self, obj):
        primary_image = obj.product.images.filter(is_primary=True).first()
        if primary_image:
            return primary_image.image.url
        return None
    
    def get_total_price(self, obj):
        return obj.total_price

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('created_at',)

class OrderSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'order_number')
