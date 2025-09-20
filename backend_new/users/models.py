from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('invoicing_user', 'InvoicingUser'),
        ('contact_user', 'ContactUser'),
    ]
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='contact_user',
        help_text='User role in the system'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    @property
    def is_admin(self):
        return self.role == 'admin'
    
    @property
    def is_invoicing_user(self):
        return self.role == 'invoicing_user'
    
    @property
    def is_contact_user(self):
        return self.role == 'contact_user'
