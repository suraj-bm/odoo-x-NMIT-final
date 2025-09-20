from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('invoicing_user', 'InvoicingUser'),
        ('contact_user', 'ContactUser'),
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('accountant', 'Accountant'),
    ]
    
    USER_TYPE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('accountant', 'Accountant'),
    ]
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='buyer',
        help_text='User role in the system'
    )
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='buyer',
        help_text='Type of user for e-commerce'
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    business_type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    @property
    def is_admin(self):
        return self.role == 'admin'
    
    @property
    def is_invoicing_user(self):
        return self.role == 'invoicing_user'
    
    @property
    def is_contact_user(self):
        return self.role == 'contact_user'
    
    @property
    def is_buyer(self):
        return self.user_type == 'buyer'
    
    @property
    def is_seller(self):
        return self.user_type == 'seller'
    
    @property
    def is_accountant(self):
        return self.user_type == 'accountant'
