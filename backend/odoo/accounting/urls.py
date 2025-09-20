from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profiles', views.UserProfileViewSet, basename='profile')
router.register(r'workcenters', views.WorkCenterViewSet, basename='workcenter')
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'workorders', views.WorkOrderViewSet, basename='workorder')
router.register(r'bom', views.BillOfMaterialsViewSet, basename='bom')
router.register(r'stock', views.StockLedgerViewSet, basename='stock')
router.register(r'reports', views.ReportViewSet, basename='report')
router.register(r'dashboard', views.DashboardViewSet, basename='dashboard')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),  # For login/logout
]
