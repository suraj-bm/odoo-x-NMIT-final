from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Company, Contact, Product, Tax, ChartOfAccounts
from .serializers import CompanySerializer, ContactSerializer, ProductSerializer, TaxSerializer, ChartOfAccountsSerializer

# Company Views
class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Company.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Company.objects.filter(created_by=self.request.user)

# Contact Views
class ContactListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Contact.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Contact.objects.filter(created_by=self.request.user)

# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(created_by=self.request.user)

# Tax Views
class TaxListCreateView(generics.ListCreateAPIView):
    serializer_class = TaxSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Tax.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaxRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaxSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Tax.objects.filter(created_by=self.request.user)

# Chart of Accounts Views
class ChartOfAccountsListCreateView(generics.ListCreateAPIView):
    serializer_class = ChartOfAccountsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return ChartOfAccounts.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ChartOfAccountsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChartOfAccountsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return ChartOfAccounts.objects.filter(created_by=self.request.user)