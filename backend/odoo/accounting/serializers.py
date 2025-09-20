from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    UserProfile, WorkCenter, Order, WorkOrder, 
    BillOfMaterials, BoMItem, StockLedger, Report
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'role', 'phone', 'department', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class WorkCenterSerializer(serializers.ModelSerializer):
    manager_name = serializers.CharField(source='manager.get_full_name', read_only=True)
    
    class Meta:
        model = WorkCenter
        fields = ['id', 'name', 'description', 'capacity', 'is_active', 'manager', 'manager_name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class OrderSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    work_center_name = serializers.CharField(source='work_center.name', read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'customer_name', 'product_name', 'quantity',
            'status', 'priority', 'due_date', 'created_by', 'created_by_name',
            'work_center', 'work_center_name', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class WorkOrderSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(source='order.order_number', read_only=True)
    product_name = serializers.CharField(source='order.product_name', read_only=True)
    assigned_to_name = serializers.CharField(source='assigned_to.get_full_name', read_only=True)
    work_center_name = serializers.CharField(source='work_center.name', read_only=True)
    
    class Meta:
        model = WorkOrder
        fields = [
            'id', 'work_order_number', 'order', 'order_number', 'product_name',
            'work_center', 'work_center_name', 'status', 'assigned_to', 'assigned_to_name',
            'start_date', 'end_date', 'estimated_hours', 'actual_hours', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class BoMItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoMItem
        fields = ['id', 'component_name', 'quantity_required', 'unit_of_measure', 
                 'unit_cost', 'supplier', 'notes']
        read_only_fields = ['id']

class BillOfMaterialsSerializer(serializers.ModelSerializer):
    items = BoMItemSerializer(many=True, read_only=True)
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    
    class Meta:
        model = BillOfMaterials
        fields = ['id', 'name', 'product_name', 'version', 'is_active', 
                 'created_by', 'created_by_name', 'items', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class StockLedgerSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    work_order_number = serializers.CharField(source='work_order.work_order_number', read_only=True)
    
    class Meta:
        model = StockLedger
        fields = [
            'id', 'item_name', 'transaction_type', 'quantity', 'unit_cost',
            'total_cost', 'reference', 'work_order', 'work_order_number',
            'created_by', 'created_by_name', 'created_at'
        ]
        read_only_fields = ['id', 'total_cost', 'created_at']

class ReportSerializer(serializers.ModelSerializer):
    generated_by_name = serializers.CharField(source='generated_by.get_full_name', read_only=True)
    
    class Meta:
        model = Report
        fields = ['id', 'name', 'report_type', 'description', 'parameters',
                 'generated_by', 'generated_by_name', 'file_path', 'created_at']
        read_only_fields = ['id', 'created_at']

# Dashboard Data Serializers
class DashboardStatsSerializer(serializers.Serializer):
    total_orders = serializers.IntegerField()
    pending_orders = serializers.IntegerField()
    completed_orders = serializers.IntegerField()
    total_work_orders = serializers.IntegerField()
    active_work_orders = serializers.IntegerField()
    total_work_centers = serializers.IntegerField()
    active_work_centers = serializers.IntegerField()
    total_stock_items = serializers.IntegerField()
    low_stock_items = serializers.IntegerField()

class WorkCenterEfficiencySerializer(serializers.Serializer):
    work_center_name = serializers.CharField()
    total_work_orders = serializers.IntegerField()
    completed_work_orders = serializers.IntegerField()
    efficiency_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)
    average_completion_time = serializers.DecimalField(max_digits=5, decimal_places=2)
