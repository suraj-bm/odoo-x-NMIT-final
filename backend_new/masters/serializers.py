from rest_framework import serializers
from .models import Company, Contact, Product, Tax, ChartOfAccounts, Category, ProductImage, ProductReview, SellerProfile, SellerProduct, SellerInvoice

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

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
    
    def get_subcategories(self, obj):
        if obj.subcategories.exists():
            return CategorySerializer(obj.subcategories.all(), many=True).data
        return []

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
        read_only_fields = ('created_at',)

class ProductReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = ProductReview
        fields = '__all__'
        read_only_fields = ('created_at',)

class ProductSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    tax_name = serializers.CharField(source='tax.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ProductReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'average_rating', 'total_reviews')

class SellerProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = SellerProfile
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class SellerProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    seller_name = serializers.CharField(source='seller.username', read_only=True)
     
    class Meta:
        model = SellerProduct
        fields = '__all__'
        read_only_fields = ('created_at', 'commission_amount')

class SellerInvoiceSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.username', read_only=True)
    
    class Meta:
        model = SellerInvoice
        fields = '__all__'
        read_only_fields = ('created_at', 'invoice_number')
