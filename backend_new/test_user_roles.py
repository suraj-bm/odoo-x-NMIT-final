#!/usr/bin/env python
import requests
import json

def test_user_roles():
    # Login first
    login_data = {'username': 'admin', 'password': 'admin123'}
    response = requests.post('http://localhost:8000/api/auth/login/', json=login_data)
    
    if response.status_code != 200:
        print(f"Login failed: {response.status_code}")
        return
    
    token = response.json()['tokens']['access']
    headers = {'Authorization': f'Bearer {token}'}
    
    print('=== TESTING USER ROLES AND API ENDPOINTS ===')
    print()
    
    # Test roles info
    print('1. Available roles and user types:')
    roles_response = requests.get('http://localhost:8000/api/auth/roles/', headers=headers)
    if roles_response.status_code == 200:
        data = roles_response.json()
        print(f"   Available roles: {[r['label'] for r in data['roles']]}")
        print(f"   Available user types: {[t['label'] for t in data['user_types']]}")
        print(f"   Current user: {data['current_user']['username']} ({data['current_user']['role']})")
    else:
        print(f"   Error: {roles_response.status_code}")
    
    print()
    
    # Test users by role
    print('2. Users by role (buyer):')
    buyer_response = requests.get('http://localhost:8000/api/auth/by-role/buyer/', headers=headers)
    if buyer_response.status_code == 200:
        data = buyer_response.json()
        print(f"   Count: {data['count']}")
        for user in data['users']:
            print(f"   - {user['username']} ({user['role_display']})")
    else:
        print(f"   Error: {buyer_response.status_code}")
    
    print()
    
    # Test users by type
    print('3. Users by type (seller):')
    seller_response = requests.get('http://localhost:8000/api/auth/by-type/seller/', headers=headers)
    if seller_response.status_code == 200:
        data = seller_response.json()
        print(f"   Count: {data['count']}")
        for user in data['users']:
            print(f"   - {user['username']} ({user['user_type_display']})")
    else:
        print(f"   Error: {seller_response.status_code}")
    
    print()
    
    print('4. Users by type (accountant):')
    accountant_response = requests.get('http://localhost:8000/api/auth/by-type/accountant/', headers=headers)
    if accountant_response.status_code == 200:
        data = accountant_response.json()
        print(f"   Count: {data['count']}")
        for user in data['users']:
            print(f"   - {user['username']} ({user['user_type_display']})")
    else:
        print(f"   Error: {accountant_response.status_code}")

if __name__ == '__main__':
    test_user_roles()
