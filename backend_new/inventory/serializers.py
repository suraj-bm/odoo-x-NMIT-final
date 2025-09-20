from rest_framework import serializers
from .models import (
    PurchaseOrder, PurchaseOrderLineItem,
    SalesOrder, SalesOrderLineItem,
    VendorBill, VendorBillLineItem,
    CustomerInvoice, CustomerInvoiceLineItem,
    StockMovement
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
