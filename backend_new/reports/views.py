from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import datetime, timedelta
from masters.models import Company, Product, Contact
from inventory.models import (
    PurchaseOrder, SalesOrder, VendorBill, CustomerInvoice, StockMovement, Order, OrderItem
)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def stock_report(request):
    """
    Stock Report - Product-wise available quantity
    """
    company_id = request.GET.get('company_id')
    
    # Get all products for the user's companies
    products_query = Product.objects.filter(created_by=request.user)
    if company_id:
        products_query = products_query.filter(company_id=company_id)
    
    stock_data = []
    
    for product in products_query:
        # Calculate stock in
        stock_in = StockMovement.objects.filter(
            product=product,
            movement_type='in',
            created_by=request.user
        ).aggregate(total=Sum('quantity'))['total'] or 0
        
        # Calculate stock out
        stock_out = StockMovement.objects.filter(
            product=product,
            movement_type='out',
            created_by=request.user
        ).aggregate(total=Sum('quantity'))['total'] or 0
        
        # Calculate available stock
        available_stock = stock_in - stock_out
        
        stock_data.append({
            'product_id': product.id,
            'product_name': product.name,
            'product_sku': product.sku,
            'unit_price': float(product.unit_price),
            'stock_in': float(stock_in),
            'stock_out': float(stock_out),
            'available_stock': float(available_stock),
            'company_name': product.company.name
        })
    
    return Response({
        'report_type': 'Stock Report',
        'generated_at': timezone.now(),
        'total_products': len(stock_data),
        'data': stock_data
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profit_loss_report(request):
    """
    P&L Report - Sales vs Purchases
    """
    company_id = request.GET.get('company_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    # Default to last 30 days if no dates provided
    if not end_date:
        end_date = timezone.now().date()
    if not start_date:
        start_date = end_date - timedelta(days=30)
    
    # Convert string dates to date objects
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    
    # Filter by company if provided
    sales_query = CustomerInvoice.objects.filter(
        created_by=request.user,
        invoice_date__range=[start_date, end_date]
    )
    purchases_query = VendorBill.objects.filter(
        created_by=request.user,
        bill_date__range=[start_date, end_date]
    )
    
    if company_id:
        sales_query = sales_query.filter(company_id=company_id)
        purchases_query = purchases_query.filter(company_id=company_id)
    
    # Calculate totals
    total_sales = sales_query.aggregate(total=Sum('total_amount'))['total'] or 0
    total_purchases = purchases_query.aggregate(total=Sum('total_amount'))['total'] or 0
    gross_profit = total_sales - total_purchases
    
    return Response({
        'report_type': 'Profit & Loss Report',
        'period': f"{start_date} to {end_date}",
        'generated_at': timezone.now(),
        'summary': {
            'total_sales': float(total_sales),
            'total_purchases': float(total_purchases),
            'gross_profit': float(gross_profit),
            'profit_margin': float((gross_profit / total_sales * 100) if total_sales > 0 else 0)
        }
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_summary(request):
    """
    Dashboard Summary - Key metrics for the dashboard
    """
    company_id = request.GET.get('company_id')
    
    # Filter by company if provided
    base_filter = {'created_by': request.user}
    if company_id:
        base_filter['company_id'] = company_id
    
    # Get counts
    total_companies = Company.objects.filter(created_by=request.user).count()
    total_products = Product.objects.filter(created_by=request.user).count()
    total_customers = Contact.objects.filter(
        contact_type__in=['customer', 'both'],
        created_by=request.user
    ).count()
    total_suppliers = Contact.objects.filter(
        contact_type__in=['supplier', 'both'],
        created_by=request.user
    ).count()
    
    # Get transaction counts
    total_purchase_orders = PurchaseOrder.objects.filter(**base_filter).count()
    total_sales_orders = SalesOrder.objects.filter(**base_filter).count()
    total_bills = VendorBill.objects.filter(**base_filter).count()
    total_invoices = CustomerInvoice.objects.filter(**base_filter).count()
    
    # Calculate totals for current month
    current_month_start = timezone.now().replace(day=1)
    current_month_sales = CustomerInvoice.objects.filter(
        **base_filter,
        invoice_date__gte=current_month_start,
        status='paid'
    ).aggregate(total=Sum('total_amount'))['total'] or 0
    
    current_month_purchases = VendorBill.objects.filter(
        **base_filter,
        bill_date__gte=current_month_start,
        status='paid'
    ).aggregate(total=Sum('total_amount'))['total'] or 0
    
    return Response({
        'report_type': 'Dashboard Summary',
        'generated_at': timezone.now(),
        'summary': {
            'total_companies': total_companies,
            'total_products': total_products,
            'total_customers': total_customers,
            'total_suppliers': total_suppliers,
            'total_purchase_orders': total_purchase_orders,
            'total_sales_orders': total_sales_orders,
            'total_bills': total_bills,
            'total_invoices': total_invoices,
            'current_month_sales': float(current_month_sales),
            'current_month_purchases': float(current_month_purchases),
            'current_month_profit': float(current_month_sales - current_month_purchases)
        }
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ecommerce_analytics(request):
    """
    E-commerce Analytics - Sales, orders, and product performance
    """
    # Get date range (last 30 days)
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=30)
    
    # Total orders
    total_orders = Order.objects.filter(created_at__date__range=[start_date, end_date]).count()
    
    # Total revenue
    total_revenue = Order.objects.filter(
        created_at__date__range=[start_date, end_date],
        status__in=['confirmed', 'shipped', 'delivered']
    ).aggregate(total=Sum('total_amount'))['total'] or 0
    
    # Total commission (10% of revenue)
    total_commission = total_revenue * 0.10
    
    # Net profit
    net_profit = total_revenue - total_commission
    
    # Top selling category
    top_category = OrderItem.objects.filter(
        order__created_at__date__range=[start_date, end_date],
        order__status__in=['confirmed', 'shipped', 'delivered']
    ).values('product__category__name').annotate(
        total_sales=Sum('quantity')
    ).order_by('-total_sales').first()
    
    # Top selling product
    top_product = OrderItem.objects.filter(
        order__created_at__date__range=[start_date, end_date],
        order__status__in=['confirmed', 'shipped', 'delivered']
    ).values('product__name').annotate(
        total_sales=Sum('quantity')
    ).order_by('-total_sales').first()
    
    # Recent orders
    recent_orders = Order.objects.filter(
        created_at__date__range=[start_date, end_date]
    ).order_by('-created_at')[:10]
    
    # Monthly sales data
    monthly_sales = []
    for i in range(6):  # Last 6 months
        month_start = (timezone.now().replace(day=1) - timedelta(days=30*i)).date()
        month_end = (month_start + timedelta(days=30)).date()
        
        month_revenue = Order.objects.filter(
            created_at__date__range=[month_start, month_end],
            status__in=['confirmed', 'shipped', 'delivered']
        ).aggregate(total=Sum('total_amount'))['total'] or 0
        
        monthly_sales.append({
            'month': month_start.strftime('%b %Y'),
            'revenue': float(month_revenue)
        })
    
    monthly_sales.reverse()
    
    return Response({
        'report_type': 'E-commerce Analytics',
        'generated_at': timezone.now(),
        'period': f"{start_date} to {end_date}",
        'summary': {
            'total_orders': total_orders,
            'total_revenue': float(total_revenue),
            'total_commission': float(total_commission),
            'net_profit': float(net_profit),
            'top_selling_category': top_category['product__category__name'] if top_category else None,
            'top_selling_product': top_product['product__name'] if top_product else None,
        },
        'recent_orders': [
            {
                'id': order.id,
                'order_number': order.order_number,
                'user_name': order.user.username,
                'total_amount': float(order.total_amount),
                'status': order.status,
                'created_at': order.created_at
            } for order in recent_orders
        ],
        'monthly_sales': monthly_sales
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_performance(request):
    """
    Product Performance Analytics
    """
    # Top selling products
    top_products = OrderItem.objects.filter(
        order__status__in=['confirmed', 'shipped', 'delivered']
    ).values(
        'product__name', 'product__category__name', 'product__unit_price'
    ).annotate(
        total_sales=Sum('quantity'),
        total_revenue=Sum('total_price')
    ).order_by('-total_sales')[:10]
    
    # Category performance
    category_performance = OrderItem.objects.filter(
        order__status__in=['confirmed', 'shipped', 'delivered']
    ).values('product__category__name').annotate(
        total_sales=Sum('quantity'),
        total_revenue=Sum('total_price')
    ).order_by('-total_sales')
    
    # Low stock products
    low_stock_products = Product.objects.filter(
        stock_quantity__lt=10,
        is_active=True
    ).values('name', 'stock_quantity', 'category__name')
    
    return Response({
        'report_type': 'Product Performance',
        'generated_at': timezone.now(),
        'top_products': list(top_products),
        'category_performance': list(category_performance),
        'low_stock_products': list(low_stock_products)
    })