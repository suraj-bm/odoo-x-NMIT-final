from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.utils import timezone
from .models import Company, Contact, Product, Tax, ChartOfAccounts, Category, ProductImage, ProductReview, SellerProfile, SellerProduct, SellerInvoice
from .serializers import CompanySerializer, ContactSerializer, ProductSerializer, TaxSerializer, ChartOfAccountsSerializer, CategorySerializer, ProductImageSerializer, ProductReviewSerializer, SellerProfileSerializer, SellerProductSerializer, SellerInvoiceSerializer

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

# Category Views
class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    queryset = Category.objects.filter(is_active=True)

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()

# Product Views (Enhanced for E-commerce)
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        category = self.request.query_params.get('category')
        subcategory = self.request.query_params.get('subcategory')
        search = self.request.query_params.get('search')
        featured = self.request.query_params.get('featured')
        
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        if subcategory:
            queryset = queryset.filter(subcategory__name__icontains=subcategory)
        if search:
            queryset = queryset.filter(name__icontains=search)
        if featured:
            queryset = queryset.filter(is_featured=True)
            
        return queryset

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(created_by=self.request.user)

# Product Review Views
class ProductReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return ProductReview.objects.filter(product_id=product_id)
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(id=product_id)
        serializer.save(user=self.request.user, product=product)
        
        # Update product rating
        reviews = ProductReview.objects.filter(product=product)
        if reviews.exists():
            avg_rating = sum(review.rating for review in reviews) / reviews.count()
            product.average_rating = round(avg_rating, 2)
            product.total_reviews = reviews.count()
            product.save()

# Product Image Views
class ProductImageListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return ProductImage.objects.filter(product_id=product_id)
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(id=product_id)
        serializer.save(product=product)

# Seller Profile Views
class SellerProfileListCreateView(generics.ListCreateAPIView):
    serializer_class = SellerProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SellerProfile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SellerProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SellerProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SellerProfile.objects.filter(user=self.request.user)

# Seller Product Views
class SellerProductListCreateView(generics.ListCreateAPIView):
    serializer_class = SellerProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SellerProduct.objects.filter(seller=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class SellerProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SellerProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SellerProduct.objects.filter(seller=self.request.user)

# Admin Views for Seller Management
class AdminSellerProductListCreateView(generics.ListCreateAPIView):
    serializer_class = SellerProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = SellerProduct.objects.all()

class AdminSellerProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SellerProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = SellerProduct.objects.all()

# Approve Seller Product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approve_seller_product(request, product_id):
    """
    Approve a seller product (Admin only)
    """
    try:
        seller_product = SellerProduct.objects.get(id=product_id)
        seller_product.is_approved = True
        seller_product.approved_by = request.user
        seller_product.approved_at = timezone.now()
        seller_product.save()
        
        # Update the main product with seller's price
        main_product = seller_product.product
        main_product.unit_price = seller_product.selling_price
        main_product.save()
        
        return Response({'message': 'Product approved successfully'}, status=status.HTTP_200_OK)
    except SellerProduct.DoesNotExist:
        return Response({'error': 'Seller product not found'}, status=status.HTTP_404_NOT_FOUND)

# Seller Invoice Views
class SellerInvoiceListCreateView(generics.ListCreateAPIView):
    serializer_class = SellerInvoiceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SellerInvoice.objects.filter(seller=self.request.user)

class SellerInvoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SellerInvoiceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SellerInvoice.objects.filter(seller=self.request.user)