from django.contrib import admin
from .models import (
    PurchaseOrder, PurchaseOrderLineItem,
    SalesOrder, SalesOrderLineItem,
    VendorBill, VendorBillLineItem,
    CustomerInvoice, CustomerInvoiceLineItem,
    StockMovement
)

class PurchaseOrderLineItemInline(admin.TabularInline):
    model = PurchaseOrderLineItem
    extra = 1

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'supplier', 'po_date', 'status', 'total_amount', 'company')
    list_filter = ('status', 'company', 'po_date')
    search_fields = ('po_number', 'supplier__name')
    inlines = [PurchaseOrderLineItemInline]
    readonly_fields = ('created_at', 'updated_at')

class SalesOrderLineItemInline(admin.TabularInline):
    model = SalesOrderLineItem
    extra = 1

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('so_number', 'customer', 'so_date', 'status', 'total_amount', 'company')
    list_filter = ('status', 'company', 'so_date')
    search_fields = ('so_number', 'customer__name')
    inlines = [SalesOrderLineItemInline]
    readonly_fields = ('created_at', 'updated_at')

class VendorBillLineItemInline(admin.TabularInline):
    model = VendorBillLineItem
    extra = 1

@admin.register(VendorBill)
class VendorBillAdmin(admin.ModelAdmin):
    list_display = ('bill_number', 'supplier', 'bill_date', 'status', 'total_amount', 'company')
    list_filter = ('status', 'company', 'bill_date')
    search_fields = ('bill_number', 'supplier__name')
    inlines = [VendorBillLineItemInline]
    readonly_fields = ('created_at', 'updated_at')

class CustomerInvoiceLineItemInline(admin.TabularInline):
    model = CustomerInvoiceLineItem
    extra = 1

@admin.register(CustomerInvoice)
class CustomerInvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer', 'invoice_date', 'status', 'total_amount', 'company')
    list_filter = ('status', 'company', 'invoice_date')
    search_fields = ('invoice_number', 'customer__name')
    inlines = [CustomerInvoiceLineItemInline]
    readonly_fields = ('created_at', 'updated_at')

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'movement_type', 'quantity', 'reference_type', 'created_at')
    list_filter = ('movement_type', 'company', 'created_at')
    search_fields = ('product__name', 'reference_type')
    readonly_fields = ('created_at',)