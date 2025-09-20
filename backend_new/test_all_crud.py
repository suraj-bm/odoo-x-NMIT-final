#!/usr/bin/env python
"""
Comprehensive CRUD Test Script - Test All Endpoints
"""

import requests
import json

def test_all_crud_endpoints():
    # Login first
    login_data = {'username': 'admin', 'password': 'admin123'}
    response = requests.post('http://localhost:8000/api/auth/login/', json=login_data)
    
    if response.status_code != 200:
        print(f"❌ Login failed: {response.status_code}")
        return
    
    token = response.json()['tokens']['access']
    headers = {'Authorization': f'Bearer {token}'}
    
    print('🔍 Testing ALL CRUD endpoints...')
    print('=' * 50)
    
    # Define all endpoints to test
    endpoints = [
        # User Management
        ('users/', 'Users'),
        
        # Master Data
        ('companies/', 'Companies'),
        ('contacts/', 'Contacts'),
        ('categories/', 'Categories'),
        ('products/', 'Products'),
        ('taxes/', 'Taxes'),
        ('chart-of-accounts/', 'Chart of Accounts'),
        
        # Seller Management
        ('sellers/seller-profiles/', 'Seller Profiles'),
        ('sellers/seller-products/', 'Seller Products'),
        ('sellers/seller-invoices/', 'Seller Invoices'),
        
        # E-commerce
        ('ecommerce/carts/', 'Carts'),
        ('ecommerce/orders/', 'Orders'),
        ('ecommerce/order-items/', 'Order Items'),
        
        # Purchase Management
        ('purchases/purchase-orders/', 'Purchase Orders'),
        
        # Sales Management
        ('sales/sales-orders/', 'Sales Orders'),
        ('sales/customer-invoices/', 'Customer Invoices'),
        
        # Inventory Management
        ('inventory/stock-movements/', 'Stock Movements'),
        
        # Reports & Analytics
        ('reports/sales-reports/', 'Sales Reports'),
        ('reports/product-analytics/', 'Product Analytics'),
    ]
    
    working_endpoints = []
    failed_endpoints = []
    
    for endpoint, name in endpoints:
        print(f'Testing {name}...')
        response = requests.get(f'http://localhost:8000/api/crud/{endpoint}', headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            count = len(data.get('results', data)) if isinstance(data, dict) else len(data)
            print(f'   ✅ {name}: {count} records')
            working_endpoints.append(name)
        else:
            print(f'   ❌ {name}: {response.status_code} - {response.text[:100]}...')
            failed_endpoints.append((name, response.status_code))
    
    print('\n' + '=' * 50)
    print('📊 SUMMARY:')
    print(f'✅ Working endpoints: {len(working_endpoints)}')
    print(f'❌ Failed endpoints: {len(failed_endpoints)}')
    
    if working_endpoints:
        print('\n✅ Working endpoints:')
        for endpoint in working_endpoints:
            print(f'   - {endpoint}')
    
    if failed_endpoints:
        print('\n❌ Failed endpoints:')
        for endpoint, status in failed_endpoints:
            print(f'   - {endpoint} ({status})')
    
    print(f'\n🎉 CRUD system is {len(working_endpoints)/(len(working_endpoints)+len(failed_endpoints))*100:.1f}% working!')

if __name__ == "__main__":
    test_all_crud_endpoints()
