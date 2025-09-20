#!/usr/bin/env python
"""
Simple CRUD Test Script
"""

import requests
import json

def test_crud_endpoints():
    # Login first
    login_data = {'username': 'admin', 'password': 'admin123'}
    response = requests.post('http://localhost:8000/api/auth/login/', json=login_data)
    
    if response.status_code != 200:
        print(f"❌ Login failed: {response.status_code}")
        return
    
    token = response.json()['tokens']['access']
    headers = {'Authorization': f'Bearer {token}'}
    
    print('🔍 Testing Fixed CRUD endpoints...')
    
    # Test users endpoint
    print('1. Testing Users endpoint...')
    response = requests.get('http://localhost:8000/api/crud/users/', headers=headers)
    print(f'   Status: {response.status_code}')
    if response.status_code == 200:
        data = response.json()
        count = len(data.get('results', data)) if isinstance(data, dict) else len(data)
        print(f'   ✅ Users: {count} records')
    else:
        print(f'   ❌ Error: {response.text[:200]}...')
    
    # Test companies endpoint
    print('2. Testing Companies endpoint...')
    response = requests.get('http://localhost:8000/api/crud/companies/', headers=headers)
    print(f'   Status: {response.status_code}')
    if response.status_code == 200:
        data = response.json()
        count = len(data.get('results', data)) if isinstance(data, dict) else len(data)
        print(f'   ✅ Companies: {count} records')
    else:
        print(f'   ❌ Error: {response.text[:200]}...')
    
    # Test categories endpoint
    print('3. Testing Categories endpoint...')
    response = requests.get('http://localhost:8000/api/crud/categories/', headers=headers)
    print(f'   Status: {response.status_code}')
    if response.status_code == 200:
        data = response.json()
        count = len(data.get('results', data)) if isinstance(data, dict) else len(data)
        print(f'   ✅ Categories: {count} records')
    else:
        print(f'   ❌ Error: {response.text[:200]}...')
    
    # Test products endpoint
    print('4. Testing Products endpoint...')
    response = requests.get('http://localhost:8000/api/crud/products/', headers=headers)
    print(f'   Status: {response.status_code}')
    if response.status_code == 200:
        data = response.json()
        count = len(data.get('results', data)) if isinstance(data, dict) else len(data)
        print(f'   ✅ Products: {count} records')
    else:
        print(f'   ❌ Error: {response.text[:200]}...')
    
    print('\n🎉 CRUD endpoints test completed!')

if __name__ == "__main__":
    test_crud_endpoints()
