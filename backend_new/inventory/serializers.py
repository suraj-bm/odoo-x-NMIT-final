from rest_framework import serializers
from .models import (
    Cart, Order, OrderItem, PurchaseOrder, PurchaseOrderLineItem,
    SalesOrder, SalesOrderLineItem, VendorBill, VendorBillLineItem,
    CustomerInvoice, CustomerInvoiceLineItem, StockMovement
)
from masters.models import Product, Contact
from users.models import User

class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.unit_price', max_digits=12, decimal_places=2, read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = [
            'id', 'user', 'product', 'product_name', 'product_price', 
            'quantity', 'total_price', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_total_price(self, obj):
        return obj.total_price

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.unit_price', max_digits=12, decimal_places=2, read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderItem
        fields = [
            'id', 'order', 'product', 'product_name', 'product_price',
            'quantity', 'unit_price', 'total_price', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_total_price(self, obj):
        return obj.total_price

class OrderSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)
    items_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'user_name', 'user_email', 'order_number', 'status',
            'subtotal', 'tax_amount', 'delivery_charge', 'total_amount',
            'shipping_address', 'payment_method', 'payment_status', 'notes',
            'order_items', 'items_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'order_number', 'created_at', 'updated_at']
    
    def get_items_count(self, obj):
        return obj.order_items.count()

class PurchaseOrderLineItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = PurchaseOrderLineItem
        fields = [
            'id', 'purchase_order', 'product', 'product_name', 'product_sku',
            'quantity', 'unit_price', 'total_price', 'received_quantity',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_total_price(self, obj):
        return obj.total_price

class PurchaseOrderSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    line_items = PurchaseOrderLineItemSerializer(many=True, read_only=True)
    items_count = serializers.SerializerMethodField()
    
    class Meta:
        model = PurchaseOrder
        fields = [
            'id', 'po_number', 'supplier', 'supplier_name', 'order_date',
            'expected_delivery_date', 'status', 'subtotal', 'tax_amount',
            'total_amount', 'notes', 'is_received', 'received_date',
            'created_by', 'created_by_name', 'line_items', 'items_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'po_number', 'created_at', 'updated_at']
    
    def get_items_count(self, obj):
        return obj.line_items.count()

class SalesOrderLineItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = SalesOrderLineItem
        fields = [
            'id', 'sales_order', 'product', 'product_name', 'product_sku',
            'quantity', 'unit_price', 'total_price', 'delivered_quantity',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_total_price(self, obj):
        return obj.total_price

class SalesOrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    line_items = SalesOrderLineItemSerializer(many=True, read_only=True)
    items_count = serializers.SerializerMethodField()
    
    class Meta:
        model = SalesOrder
        fields = [
            'id', 'so_number', 'customer', 'customer_name', 'order_date',
            'expected_delivery_date', 'status', 'subtotal', 'tax_amount',
            'total_amount', 'notes', 'is_delivered', 'delivered_date',
            'created_by', 'created_by_name', 'line_items', 'items_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'so_number', 'created_at', 'updated_at']
    
    def get_items_count(self, obj):
        return obj.line_items.count()

class CustomerInvoiceLineItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = CustomerInvoiceLineItem
        fields = [
            'id', 'invoice', 'product', 'product_name', 'product_sku',
            'quantity', 'unit_price', 'total_price', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_total_price(self, obj):
        return obj.total_price

class CustomerInvoiceSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    line_items = CustomerInvoiceLineItemSerializer(many=True, read_only=True)
    items_count = serializers.SerializerMethodField()
    
    class Meta:
        model = CustomerInvoice
        fields = [
            'id', 'invoice_number', 'customer', 'customer_name', 'invoice_date',
            'due_date', 'status', 'subtotal', 'tax_amount', 'total_amount',
            'notes', 'is_paid', 'paid_date', 'payment_method',
            'created_by', 'created_by_name', 'line_items', 'items_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'invoice_number', 'created_at', 'updated_at']
    
    def get_items_count(self, obj):
        return obj.line_items.count()

class VendorBillLineItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = VendorBillLineItem
        fields = [
            'id', 'vendor_bill', 'product', 'product_name', 'product_sku',
            'quantity', 'unit_price', 'total_price', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_total_price(self, obj):
        return obj.total_price

class VendorBillSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    line_items = VendorBillLineItemSerializer(many=True, read_only=True)
    items_count = serializers.SerializerMethodField()
    
    class Meta:
        model = VendorBill
        fields = [
            'id', 'bill_number', 'vendor', 'vendor_name', 'bill_date',
            'due_date', 'status', 'subtotal', 'tax_amount', 'total_amount',
            'notes', 'is_paid', 'paid_date', 'payment_method',
            'created_by', 'created_by_name', 'line_items', 'items_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'bill_number', 'created_at', 'updated_at']
    
    def get_items_count(self, obj):
        return obj.line_items.count()

class StockMovementSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = StockMovement
        fields = [
            'id', 'product', 'product_name', 'product_sku', 'movement_type',
            'quantity', 'reference_type', 'reference_id', 'notes',
            'created_by', 'created_by_name', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']