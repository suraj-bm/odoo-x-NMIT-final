#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'odoo.odoo.settings')
django.setup()

from django.contrib.auth.models import User
from accounting.models import UserProfile

# Create superuser
if not User.objects.filter(username='admin').exists():
    user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )
    
    # Create profile for admin
    UserProfile.objects.create(
        user=user,
        role='admin_business_owner',
        phone='1234567890',
        department='IT'
    )
    
    print("Superuser 'admin' created with password 'admin123'")
    print("Admin profile created with role 'Admin / Business Owner'")
else:
    print("Superuser 'admin' already exists")
