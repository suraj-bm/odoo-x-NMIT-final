#!/usr/bin/env python
"""
Comprehensive CRUD Operations Test Script
Tests all CRUD operations for all models in the system
"""

import requests
import json
import time

class CRUDTester:
    def __init__(self, base_url="http://localhost:8000/api"):
        self.base_url = base_url
        self.token = None
        self.session = requests.Session()
        
    def login(self, username="admin", password="admin123"):
        """Login and get authentication token"""
        login_data = {
            "username": username,
            "password": password
        }
        
        response = self.session.post(f"{self.base_url}/auth/login/", json=login_data)
        if response.status_code == 200:
            data = response.json()
            self.token = data['tokens']['access']
            self.session.headers.update({
                'Authorization': f'Bearer {self.token}',
                'Content-Type': 'application/json'
            })
            print(f"✅ Login successful as {username}")
            return True
        else:
            print(f"❌ Login failed: {response.status_code} - {response.text}")
            return False
    
    def test_crud_operation(self, endpoint, model_name, test_data, update_data=None):
        """Test full CRUD operations for a given endpoint"""
        print(f"\n🔍 Testing CRUD operations for {model_name}")
        print("=" * 50)
        
        # CREATE
        print("1. Testing CREATE...")
        create_response = self.session.post(f"{self.base_url}/crud/{endpoint}/", json=test_data)
        if create_response.status_code in [200, 201]:
            created_data = create_response.json()
            created_id = created_data.get('id')
            print(f"   ✅ Created {model_name} with ID: {created_id}")
        else:
            print(f"   ❌ Create failed: {create_response.status_code} - {create_response.text}")
            return False
        
        # READ (List)
        print("2. Testing READ (List)...")
        list_response = self.session.get(f"{self.base_url}/crud/{endpoint}/")
        if list_response.status_code == 200:
            list_data = list_response.json()
            print(f"   ✅ Retrieved {len(list_data.get('results', list_data))} {model_name} records")
        else:
            print(f"   ❌ List failed: {list_response.status_code} - {list_response.text}")
        
        # READ (Detail)
        print("3. Testing READ (Detail)...")
        detail_response = self.session.get(f"{self.base_url}/crud/{endpoint}/{created_id}/")
        if detail_response.status_code == 200:
            detail_data = detail_response.json()
            print(f"   ✅ Retrieved {model_name} detail for ID: {created_id}")
        else:
            print(f"   ❌ Detail failed: {detail_response.status_code} - {detail_response.text}")
        
        # UPDATE
        if update_data:
            print("4. Testing UPDATE...")
            update_response = self.session.put(f"{self.base_url}/crud/{endpoint}/{created_id}/", json=update_data)
            if update_response.status_code == 200:
                updated_data = update_response.json()
                print(f"   ✅ Updated {model_name} with ID: {created_id}")
            else:
                print(f"   ❌ Update failed: {update_response.status_code} - {update_response.text}")
        
        # DELETE
        print("5. Testing DELETE...")
        delete_response = self.session.delete(f"{self.base_url}/crud/{endpoint}/{created_id}/")
        if delete_response.status_code in [200, 204]:
            print(f"   ✅ Deleted {model_name} with ID: {created_id}")
        else:
            print(f"   ❌ Delete failed: {delete_response.status_code} - {delete_response.text}")
        
        return True
    
    def test_bulk_operations(self, model_name, test_data_list):
        """Test bulk operations"""
        print(f"\n🔍 Testing Bulk Operations for {model_name}")
        print("=" * 50)
        
        # Create multiple records
        created_ids = []
        for i, test_data in enumerate(test_data_list):
            response = self.session.post(f"{self.base_url}/crud/{model_name}/", json=test_data)
            if response.status_code in [200, 201]:
                created_data = response.json()
                created_ids.append(created_data.get('id'))
                print(f"   ✅ Created {model_name} {i+1} with ID: {created_data.get('id')}")
            else:
                print(f"   ❌ Create {i+1} failed: {response.status_code}")
        
        if created_ids:
            # Test bulk update
            print(f"\n   Testing bulk update for {len(created_ids)} records...")
            bulk_update_data = {
                "ids": created_ids,
                "update_data": {"is_active": False}
            }
            bulk_update_response = self.session.post(f"{self.base_url}/crud/bulk/update/{model_name}/", json=bulk_update_data)
            if bulk_update_response.status_code == 200:
                print(f"   ✅ Bulk update successful")
            else:
                print(f"   ❌ Bulk update failed: {bulk_update_response.status_code}")
            
            # Test bulk delete
            print(f"\n   Testing bulk delete for {len(created_ids)} records...")
            bulk_delete_data = {"ids": created_ids}
            bulk_delete_response = self.session.post(f"{self.base_url}/crud/bulk/delete/{model_name}/", json=bulk_delete_data)
            if bulk_delete_response.status_code == 200:
                print(f"   ✅ Bulk delete successful")
            else:
                print(f"   ❌ Bulk delete failed: {bulk_delete_response.status_code}")
    
    def run_all_tests(self):
        """Run all CRUD tests"""
        print("🚀 Starting Comprehensive CRUD Operations Test")
        print("=" * 60)
        
        if not self.login():
            return False
        
        # Test data for different models
        test_cases = [
            {
                "endpoint": "masters/companies",
                "model_name": "Company",
                "test_data": {
                    "name": "Test Company",
                    "email": "test@company.com",
                    "phone": "+1234567890",
                    "address": "123 Test Street",
                    "is_active": True
                },
                "update_data": {
                    "name": "Updated Test Company",
                    "email": "updated@company.com"
                }
            },
            {
                "endpoint": "masters/categories",
                "model_name": "Category",
                "test_data": {
                    "name": "Test Category",
                    "description": "Test category description",
                    "is_active": True
                },
                "update_data": {
                    "name": "Updated Test Category",
                    "description": "Updated description"
                }
            },
            {
                "endpoint": "masters/taxes",
                "model_name": "Tax",
                "test_data": {
                    "name": "Test Tax",
                    "rate": 18.0,
                    "description": "Test tax description",
                    "is_active": True
                },
                "update_data": {
                    "name": "Updated Test Tax",
                    "rate": 20.0
                }
            },
            {
                "endpoint": "ecommerce/carts",
                "model_name": "Cart",
                "test_data": {
                    "product": 1,  # Assuming product with ID 1 exists
                    "quantity": 2
                },
                "update_data": {
                    "quantity": 3
                }
            }
        ]
        
        # Run individual CRUD tests
        for test_case in test_cases:
            try:
                self.test_crud_operation(
                    test_case["endpoint"],
                    test_case["model_name"],
                    test_case["test_data"],
                    test_case.get("update_data")
                )
                time.sleep(1)  # Small delay between tests
            except Exception as e:
                print(f"❌ Error testing {test_case['model_name']}: {str(e)}")
        
        # Test bulk operations
        bulk_test_data = [
            {"name": f"Bulk Test Company {i}", "email": f"bulk{i}@test.com", "is_active": True}
            for i in range(1, 4)
        ]
        
        try:
            self.test_bulk_operations("masters/companies", bulk_test_data)
        except Exception as e:
            print(f"❌ Error testing bulk operations: {str(e)}")
        
        print("\n🎉 CRUD Operations Test Completed!")
        return True

def main():
    """Main function to run the tests"""
    tester = CRUDTester()
    tester.run_all_tests()

if __name__ == "__main__":
    main()
