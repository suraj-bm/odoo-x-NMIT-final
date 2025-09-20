from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from .models import (
    PurchaseOrder, PurchaseOrderLineItem,
    SalesOrder, SalesOrderLineItem,
    VendorBill, VendorBillLineItem,
    CustomerInvoice, CustomerInvoiceLineItem,
    StockMovement
)
from .serializers import (
    PurchaseOrderSerializer, SalesOrderSerializer,
    VendorBillSerializer, CustomerInvoiceSerializer,
    StockMovementSerializer
)

# Purchase Order Views
class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return PurchaseOrder.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return PurchaseOrder.objects.filter(created_by=self.request.user)

# Sales Order Views
class SalesOrderListCreateView(generics.ListCreateAPIView):
    serializer_class = SalesOrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SalesOrder.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SalesOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SalesOrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SalesOrder.objects.filter(created_by=self.request.user)

# Vendor Bill Views
class VendorBillListCreateView(generics.ListCreateAPIView):
    serializer_class = VendorBillSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return VendorBill.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class VendorBillRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VendorBillSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return VendorBill.objects.filter(created_by=self.request.user)

# Customer Invoice Views
class CustomerInvoiceListCreateView(generics.ListCreateAPIView):
    serializer_class = CustomerInvoiceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return CustomerInvoice.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CustomerInvoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerInvoiceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return CustomerInvoice.objects.filter(created_by=self.request.user)

# Stock Movement Views
class StockMovementListCreateView(generics.ListCreateAPIView):
    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return StockMovement.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Convert PO to Bill
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def convert_po_to_bill(request, po_id):
    try:
        po = PurchaseOrder.objects.get(id=po_id, created_by=request.user)
        
        if po.status != 'confirmed':
            return Response({'error': 'Purchase Order must be confirmed to convert to bill'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        with transaction.atomic():
            # Create Vendor Bill
            bill = VendorBill.objects.create(
                company=po.company,
                supplier=po.supplier,
                purchase_order=po,
                bill_date=po.po_date,
                due_date=po.expected_delivery_date,
                subtotal=po.subtotal,
                tax_amount=po.tax_amount,
                total_amount=po.total_amount,
                notes=po.notes,
                created_by=request.user
            )
            
            # Create Bill Line Items
            for po_item in po.line_items.all():
                VendorBillLineItem.objects.create(
                    vendor_bill=bill,
                    product=po_item.product,
                    quantity=po_item.quantity,
                    unit_price=po_item.unit_price,
                    line_total=po_item.line_total
                )
            
            # Update PO status
            po.status = 'received'
            po.save()
            
            # Create stock movement
            for po_item in po.line_items.all():
                StockMovement.objects.create(
                    company=po.company,
                    product=po_item.product,
                    movement_type='in',
                    quantity=po_item.quantity,
                    reference_type='purchase_order',
                    reference_id=po.id,
                    notes=f'Stock in from PO-{po.po_number}',
                    created_by=request.user
                )
        
        serializer = VendorBillSerializer(bill)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase Order not found'}, status=status.HTTP_404_NOT_FOUND)

# Convert SO to Invoice
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def convert_so_to_invoice(request, so_id):
    try:
        so = SalesOrder.objects.get(id=so_id, created_by=request.user)
        
        if so.status != 'confirmed':
            return Response({'error': 'Sales Order must be confirmed to convert to invoice'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        with transaction.atomic():
            # Create Customer Invoice
            invoice = CustomerInvoice.objects.create(
                company=so.company,
                customer=so.customer,
                sales_order=so,
                invoice_date=so.so_date,
                due_date=so.expected_delivery_date,
                subtotal=so.subtotal,
                tax_amount=so.tax_amount,
                total_amount=so.total_amount,
                notes=so.notes,
                created_by=request.user
            )
            
            # Create Invoice Line Items
            for so_item in so.line_items.all():
                CustomerInvoiceLineItem.objects.create(
                    customer_invoice=invoice,
                    product=so_item.product,
                    quantity=so_item.quantity,
                    unit_price=so_item.unit_price,
                    line_total=so_item.line_total
                )
            
            # Update SO status
            so.status = 'delivered'
            so.save()
            
            # Create stock movement
            for so_item in so.line_items.all():
                StockMovement.objects.create(
                    company=so.company,
                    product=so_item.product,
                    movement_type='out',
                    quantity=so_item.quantity,
                    reference_type='sales_order',
                    reference_id=so.id,
                    notes=f'Stock out from SO-{so.so_number}',
                    created_by=request.user
                )
        
        serializer = CustomerInvoiceSerializer(invoice)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    except SalesOrder.DoesNotExist:
        return Response({'error': 'Sales Order not found'}, status=status.HTTP_404_NOT_FOUND)