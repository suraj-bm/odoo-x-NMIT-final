from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()

class Command(BaseCommand):
    help = 'Create test users with different roles for testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Reset all test users before creating new ones',
        )

    def handle(self, *args, **options):
        if options['reset']:
            self.stdout.write('Resetting test users...')
            User.objects.filter(username__startswith='test_').delete()
            User.objects.filter(username__in=['admin', 'buyer', 'seller', 'accountant']).delete()

        with transaction.atomic():
            # Create admin user
            admin_user, created = User.objects.get_or_create(
                username='admin',
                defaults={
                    'email': 'admin@example.com',
                    'first_name': 'Admin',
                    'last_name': 'User',
                    'role': 'admin',
                    'user_type': 'buyer',
                    'is_staff': True,
                    'is_superuser': True,
                    'is_active': True,
                }
            )
            if created:
                admin_user.set_password('admin123')
                admin_user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Created admin user: {admin_user.username}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Admin user already exists: {admin_user.username}')
                )

            # Create buyer user
            buyer_user, created = User.objects.get_or_create(
                username='buyer',
                defaults={
                    'email': 'buyer@example.com',
                    'first_name': 'John',
                    'last_name': 'Buyer',
                    'role': 'buyer',
                    'user_type': 'buyer',
                    'phone': '+1234567890',
                    'address': '123 Main St',
                    'city': 'New York',
                    'state': 'NY',
                    'postal_code': '10001',
                    'is_active': True,
                }
            )
            if created:
                buyer_user.set_password('buyer123')
                buyer_user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Created buyer user: {buyer_user.username}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Buyer user already exists: {buyer_user.username}')
                )

            # Create seller user
            seller_user, created = User.objects.get_or_create(
                username='seller',
                defaults={
                    'email': 'seller@example.com',
                    'first_name': 'Jane',
                    'last_name': 'Seller',
                    'role': 'seller',
                    'user_type': 'seller',
                    'phone': '+1234567891',
                    'address': '456 Oak Ave',
                    'city': 'Los Angeles',
                    'state': 'CA',
                    'postal_code': '90210',
                    'business_name': 'Jane\'s Furniture Store',
                    'business_type': 'Retail',
                    'is_active': True,
                }
            )
            if created:
                seller_user.set_password('seller123')
                seller_user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Created seller user: {seller_user.username}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Seller user already exists: {seller_user.username}')
                )

            # Create accountant user
            accountant_user, created = User.objects.get_or_create(
                username='accountant',
                defaults={
                    'email': 'accountant@example.com',
                    'first_name': 'Bob',
                    'last_name': 'Accountant',
                    'role': 'accountant',
                    'user_type': 'accountant',
                    'phone': '+1234567892',
                    'address': '789 Pine St',
                    'city': 'Chicago',
                    'state': 'IL',
                    'postal_code': '60601',
                    'business_name': 'Bob\'s Accounting Services',
                    'business_type': 'Professional Services',
                    'is_active': True,
                }
            )
            if created:
                accountant_user.set_password('accountant123')
                accountant_user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Created accountant user: {accountant_user.username}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Accountant user already exists: {accountant_user.username}')
                )

        self.stdout.write(
            self.style.SUCCESS('\nTest users created successfully!')
        )
        self.stdout.write('\nLogin credentials:')
        self.stdout.write('Admin: admin / admin123')
        self.stdout.write('Buyer: buyer / buyer123')
        self.stdout.write('Seller: seller / seller123')
        self.stdout.write('Accountant: accountant / accountant123')
