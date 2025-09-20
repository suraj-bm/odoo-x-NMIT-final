from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from masters.models import Company, Category, Product, Tax
from inventory.models import StockMovement

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed e-commerce sample data'

    def handle(self, *args, **options):
        # Create sample company
        company, created = Company.objects.get_or_create(
            name="Shiv Furniture Store",
            defaults={
                'address': '123 Main Street, Mumbai',
                'city': 'Mumbai',
                'state': 'Maharashtra',
                'country': 'India',
                'postal_code': '400001',
                'phone': '+91-9876543210',
                'email': 'info@shivfurniture.com',
                'tax_id': 'GST123456789',
                'created_by': User.objects.first()
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created company: Shiv Furniture Store'))
        
        # Create categories
        categories_data = [
            {'name': 'Furniture', 'description': 'All types of furniture'},
            {'name': 'Electronics', 'description': 'Electronic items'},
            {'name': 'Home Decor', 'description': 'Home decoration items'},
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
        
        # Create subcategories
        furniture = Category.objects.get(name='Furniture')
        subcategories_data = [
            {'name': 'Chairs', 'parent': furniture, 'description': 'All types of chairs'},
            {'name': 'Tables', 'parent': furniture, 'description': 'All types of tables'},
            {'name': 'Sofas', 'parent': furniture, 'description': 'All types of sofas'},
            {'name': 'Beds', 'parent': furniture, 'description': 'All types of beds'},
        ]
        
        for subcat_data in subcategories_data:
            subcategory, created = Category.objects.get_or_create(
                name=subcat_data['name'],
                parent=subcat_data['parent'],
                defaults=subcat_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created subcategory: {subcategory.name}'))
        
        # Create tax
        tax, created = Tax.objects.get_or_create(
            name="GST 18%",
            defaults={
                'rate': 18.0,
                'tax_type': 'percentage',
                'company': company,
                'created_by': User.objects.first()
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created tax: GST 18%'))
        
        # Create sample products
        products_data = [
            {
                'name': 'Wooden Office Chair',
                'description': 'Comfortable wooden office chair with cushion',
                'sku': 'WO-001',
                'unit_price': 2500.00,
                'cost_price': 1500.00,
                'category': Category.objects.get(name='Chairs'),
                'manufacturer': 'Furniture Co.',
                'delivery_time': '3-5 days',
                'stock_quantity': 50,
                'is_featured': True
            },
            {
                'name': 'Modern Dining Table',
                'description': '6-seater modern dining table',
                'sku': 'DT-001',
                'unit_price': 15000.00,
                'cost_price': 10000.00,
                'category': Category.objects.get(name='Tables'),
                'manufacturer': 'Table Masters',
                'delivery_time': '5-7 days',
                'stock_quantity': 20,
                'is_featured': True
            },
            {
                'name': 'Leather Sofa Set',
                'description': '3+2+1 leather sofa set',
                'sku': 'LS-001',
                'unit_price': 45000.00,
                'cost_price': 30000.00,
                'category': Category.objects.get(name='Sofas'),
                'manufacturer': 'Sofa World',
                'delivery_time': '7-10 days',
                'stock_quantity': 10,
                'is_featured': True
            },
            {
                'name': 'King Size Bed',
                'description': 'King size bed with storage',
                'sku': 'KB-001',
                'unit_price': 25000.00,
                'cost_price': 18000.00,
                'category': Category.objects.get(name='Beds'),
                'manufacturer': 'Bed Crafters',
                'delivery_time': '10-15 days',
                'stock_quantity': 15,
                'is_featured': False
            },
            {
                'name': 'Plastic Chair',
                'description': 'Lightweight plastic chair',
                'sku': 'PC-001',
                'unit_price': 500.00,
                'cost_price': 300.00,
                'category': Category.objects.get(name='Chairs'),
                'manufacturer': 'Plastic Works',
                'delivery_time': '2-3 days',
                'stock_quantity': 100,
                'is_featured': False
            }
        ]
        
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                sku=product_data['sku'],
                defaults={
                    **product_data,
                    'company': company,
                    'tax': tax,
                    'product_type': 'goods',
                    'created_by': User.objects.first()
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
        
        self.stdout.write(self.style.SUCCESS('E-commerce data seeded successfully!'))
