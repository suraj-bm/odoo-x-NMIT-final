#!/usr/bin/env python
"""
Check which models have is_active field
"""

from masters.models import SellerProfile, SellerProduct, SellerInvoice
from inventory.models import PurchaseOrder, SalesOrder, CustomerInvoice
from reports.models import SalesReport, ProductAnalytics

# Check which models have is_active field
models_to_check = [
    (SellerProfile, 'SellerProfile'),
    (SellerProduct, 'SellerProduct'), 
    (SellerInvoice, 'SellerInvoice'),
    (PurchaseOrder, 'PurchaseOrder'),
    (SalesOrder, 'SalesOrder'),
    (CustomerInvoice, 'CustomerInvoice'),
    (SalesReport, 'SalesReport'),
    (ProductAnalytics, 'ProductAnalytics'),
]

print("Checking models for is_active field:")
print("=" * 40)

for model, name in models_to_check:
    fields = [field.name for field in model._meta.fields]
    has_is_active = 'is_active' in fields
    status = "✅" if has_is_active else "❌"
    print(f'{name}: {status} is_active field')

print("\nModels missing is_active field need to be updated.")
