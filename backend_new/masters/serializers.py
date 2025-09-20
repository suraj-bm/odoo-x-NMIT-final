from rest_framework import serializers
from .models import Company, Contact, Product, Tax, ChartOfAccounts

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by')

class ContactSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by')

class ProductSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    tax_name = serializers.CharField(source='tax.name', read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by')

class TaxSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    
    class Meta:
        model = Tax
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by')

class ChartOfAccountsSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    parent_name = serializers.CharField(source='parent.name', read_only=True)
    
    class Meta:
        model = ChartOfAccounts
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by')
