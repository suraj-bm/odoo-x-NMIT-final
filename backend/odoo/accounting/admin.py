from django.contrib import admin

# Register your models here.
from .models import (
    UserProfile,
    WorkCenter,
    Order,
    WorkOrder,
    BillOfMaterials,
    BoMItem,
    StockLedger,
    Report
)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone', 'department', 'created_at')
    list_filter = ('role', 'department')
    search_fields = ('user__username', 'phone', 'department')

@admin.register(WorkCenter)
class WorkCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'capacity', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'product_name', 'status', 'priority', 'due_date', 'created_by')
    list_filter = ('status', 'priority')
    search_fields = ('order_number', 'customer_name', 'product_name')

# Repeat similarly for WorkOrder, BillOfMaterials, BoMItem, StockLedger, Report
@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('work_order_number', 'order', 'work_center', 'status', 'start_date', 'end_date')
    list_filter = ('status',)
    search_fields = ('work_order_number', 'order__order_number')    
@admin.register(BillOfMaterials)
class BillOfMaterialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_name', 'version', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'product_name')
@admin.register(BoMItem)
class BoMItemAdmin(admin.ModelAdmin):
    list_display = ('bom', 'component_name', 'quantity_required', 'unit_of_measure', 'unit_cost', 'supplier')
    list_filter = ('unit_of_measure',)
    search_fields = ('component_name', 'supplier')
@admin.register(StockLedger)
class StockLedgerAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'transaction_type', 'quantity', 'unit_cost', 'total_cost', 'reference', 'work_order', 'created_by', 'created_at')
    list_filter = ('transaction_type',)
    search_fields = ('item_name', 'reference', 'work_order__work_order_number', 'created_by__username')
