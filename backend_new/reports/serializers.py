from rest_framework import serializers
from .models import SalesReport, ProductAnalytics
from masters.models import Product
from users.models import User

class SalesReportSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = SalesReport
        fields = [
            'id', 'report_name', 'report_type', 'report_date', 'start_date',
            'end_date', 'total_sales', 'total_orders', 'total_customers',
            'average_order_value', 'top_products', 'sales_by_category',
            'sales_by_month', 'is_generated', 'created_by', 'created_by_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class ProductAnalyticsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = ProductAnalytics
        fields = [
            'id', 'product', 'product_name', 'product_sku', 'analytics_type',
            'analytics_date', 'views_count', 'sales_count', 'revenue',
            'conversion_rate', 'average_rating', 'total_reviews',
            'stock_level', 'low_stock_alert', 'created_by', 'created_by_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
