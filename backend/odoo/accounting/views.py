from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Count, Q, Avg, Sum
from django.utils import timezone
from datetime import timedelta
from .models import (
    UserProfile, WorkCenter, Order, WorkOrder, 
    BillOfMaterials, BoMItem, StockLedger, Report
)
from .serializers import (
    UserProfileSerializer, WorkCenterSerializer, OrderSerializer,
    WorkOrderSerializer, BillOfMaterialsSerializer, BoMItemSerializer,
    StockLedgerSerializer, ReportSerializer, DashboardStatsSerializer,
    WorkCenterEfficiencySerializer
)

# Auth & Profile Views
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Users can only see their own profile unless they're admin
        if self.request.user.is_staff:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def me(self, request):
        """Get current user's profile"""
        try:
            profile = UserProfile.objects.get(user=request.user)
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

# Work Centers Views
class WorkCenterViewSet(viewsets.ModelViewSet):
    queryset = WorkCenter.objects.all()
    serializer_class = WorkCenterSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def efficiency(self, request, pk=None):
        """Get work center efficiency data"""
        work_center = self.get_object()
        
        # Calculate efficiency metrics
        total_work_orders = WorkOrder.objects.filter(work_center=work_center).count()
        completed_work_orders = WorkOrder.objects.filter(
            work_center=work_center, 
            status='completed'
        ).count()
        
        efficiency_percentage = (completed_work_orders / total_work_orders * 100) if total_work_orders > 0 else 0
        
        data = {
            'work_center_name': work_center.name,
            'total_work_orders': total_work_orders,
            'completed_work_orders': completed_work_orders,
            'efficiency_percentage': round(efficiency_percentage, 2),
            'average_completion_time': 0  # Simplified for now
        }
        
        serializer = WorkCenterEfficiencySerializer(data)
        return Response(serializer.data)

# Orders Views
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter by user role
        try:
            profile = UserProfile.objects.get(user=self.request.user)
            if profile.role == 'manufacturing_manager':
                return Order.objects.all()
            elif profile.role == 'operator_worker':
                return Order.objects.filter(work_orders__assigned_to=self.request.user).distinct()
            else:
                return Order.objects.filter(created_by=self.request.user)
        except UserProfile.DoesNotExist:
            return Order.objects.filter(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def create_work_order(self, request, pk=None):
        """Create work order for an order"""
        order = self.get_object()
        work_center_id = request.data.get('work_center_id')
        
        if not work_center_id:
            return Response({'error': 'Work center ID required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            work_center = WorkCenter.objects.get(id=work_center_id)
        except WorkCenter.DoesNotExist:
            return Response({'error': 'Work center not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Generate work order number
        wo_count = WorkOrder.objects.count() + 1
        wo_number = f"WO-{wo_count:06d}"
        
        work_order = WorkOrder.objects.create(
            work_order_number=wo_number,
            order=order,
            work_center=work_center,
            assigned_to=request.data.get('assigned_to'),
            estimated_hours=request.data.get('estimated_hours', 0),
            notes=request.data.get('notes', '')
        )
        
        serializer = WorkOrderSerializer(work_order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Work Orders Views
class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter by user role
        try:
            profile = UserProfile.objects.get(user=self.request.user)
            if profile.role == 'manufacturing_manager':
                return WorkOrder.objects.all()
            elif profile.role == 'operator_worker':
                return WorkOrder.objects.filter(assigned_to=self.request.user)
            else:
                return WorkOrder.objects.all()
        except UserProfile.DoesNotExist:
            return WorkOrder.objects.filter(assigned_to=self.request.user)

    @action(detail=True, methods=['post'])
    def start_work(self, request, pk=None):
        """Start work on a work order"""
        work_order = self.get_object()
        if work_order.status != 'ready':
            return Response({'error': 'Work order must be ready to start'}, status=status.HTTP_400_BAD_REQUEST)
        
        work_order.status = 'in_progress'
        work_order.start_date = timezone.now()
        work_order.save()
        
        serializer = self.get_serializer(work_order)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def complete_work(self, request, pk=None):
        """Complete a work order"""
        work_order = self.get_object()
        if work_order.status != 'in_progress':
            return Response({'error': 'Work order must be in progress to complete'}, status=status.HTTP_400_BAD_REQUEST)
        
        work_order.status = 'completed'
        work_order.end_date = timezone.now()
        work_order.actual_hours = request.data.get('actual_hours', work_order.actual_hours)
        work_order.save()
        
        serializer = self.get_serializer(work_order)
        return Response(serializer.data)

# Bill of Materials Views
class BillOfMaterialsViewSet(viewsets.ModelViewSet):
    queryset = BillOfMaterials.objects.all()
    serializer_class = BillOfMaterialsSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        """Add item to BoM"""
        bom = self.get_object()
        serializer = BoMItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(bom=bom)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Stock Ledger Views
class StockLedgerViewSet(viewsets.ModelViewSet):
    queryset = StockLedger.objects.all()
    serializer_class = StockLedgerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter by user role
        try:
            profile = UserProfile.objects.get(user=self.request.user)
            if profile.role in ['inventory_manager', 'admin_business_owner']:
                return StockLedger.objects.all()
            else:
                return StockLedger.objects.filter(created_by=self.request.user)
        except UserProfile.DoesNotExist:
            return StockLedger.objects.filter(created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def inventory_summary(self, request):
        """Get inventory summary"""
        # Group by item name and calculate totals
        from django.db.models import Sum
        summary = StockLedger.objects.values('item_name').annotate(
            total_in=Sum('quantity', filter=Q(transaction_type='in')),
            total_out=Sum('quantity', filter=Q(transaction_type='out')),
            current_stock=Sum('quantity', filter=Q(transaction_type='in')) - Sum('quantity', filter=Q(transaction_type='out'))
        ).order_by('item_name')
        
        return Response(list(summary))

# Reports Views
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def generate_production_report(self, request):
        """Generate production report"""
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        # Filter work orders by date range
        work_orders = WorkOrder.objects.all()
        if start_date:
            work_orders = work_orders.filter(created_at__gte=start_date)
        if end_date:
            work_orders = work_orders.filter(created_at__lte=end_date)
        
        # Calculate metrics
        total_work_orders = work_orders.count()
        completed_orders = work_orders.filter(status='completed').count()
        in_progress_orders = work_orders.filter(status='in_progress').count()
        
        # Work center breakdown
        work_center_stats = work_orders.values('work_center__name').annotate(
            total=Count('id'),
            completed=Count('id', filter=Q(status='completed'))
        )
        
        data = {
            'period': {'start': start_date, 'end': end_date},
            'summary': {
                'total_work_orders': total_work_orders,
                'completed_orders': completed_orders,
                'in_progress_orders': in_progress_orders,
                'completion_rate': (completed_orders / total_work_orders * 100) if total_work_orders > 0 else 0
            },
            'work_center_breakdown': list(work_center_stats)
        }
        
        return Response(data)

# Dashboard Views
class DashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get dashboard statistics"""
        # Basic counts
        total_orders = Order.objects.count()
        pending_orders = Order.objects.filter(status='pending').count()
        completed_orders = Order.objects.filter(status='completed').count()
        
        total_work_orders = WorkOrder.objects.count()
        active_work_orders = WorkOrder.objects.filter(status='in_progress').count()
        
        total_work_centers = WorkCenter.objects.count()
        active_work_centers = WorkCenter.objects.filter(is_active=True).count()
        
        # Stock summary
        stock_items = StockLedger.objects.values('item_name').distinct().count()
        low_stock_items = 0  # Simplified for now
        
        data = {
            'total_orders': total_orders,
            'pending_orders': pending_orders,
            'completed_orders': completed_orders,
            'total_work_orders': total_work_orders,
            'active_work_orders': active_work_orders,
            'total_work_centers': total_work_centers,
            'active_work_centers': active_work_centers,
            'total_stock_items': stock_items,
            'low_stock_items': low_stock_items
        }
        
        serializer = DashboardStatsSerializer(data)
        return Response(serializer.data)
