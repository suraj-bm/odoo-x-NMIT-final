# 🔧 Comprehensive CRUD API Documentation

## Overview

This document provides complete documentation for all CRUD (Create, Read, Update, Delete) operations available in the e-commerce platform. All endpoints require authentication via JWT token.

## Authentication

All CRUD endpoints require authentication. Include the JWT token in the Authorization header:

```bash
Authorization: Bearer YOUR_JWT_TOKEN
```

## Base URL

```
http://localhost:8000/api/crud/
```

## Pagination

All list endpoints support pagination:

- `page` - Page number (default: 1)
- `page_size` - Items per page (default: 20, max: 100)
- `search` - Search term
- `ordering` - Order by field (prefix with `-` for descending)

## Filtering

Most endpoints support filtering using query parameters:

- `is_active` - Filter by active status
- `created_at` - Filter by creation date
- `updated_at` - Filter by update date

---

## 📊 **USER MANAGEMENT**

### Users

**Base Endpoint:** `/users/`

#### List Users
```http
GET /api/crud/users/
```

**Query Parameters:**
- `role` - Filter by user role
- `user_type` - Filter by user type
- `is_active` - Filter by active status
- `search` - Search in username, email, first_name, last_name, business_name

**Response:**
```json
{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "username": "admin",
      "email": "admin@example.com",
      "first_name": "Admin",
      "last_name": "User",
      "role": "admin",
      "role_display": "Admin",
      "user_type": "buyer",
      "user_type_display": "Buyer",
      "phone": "+1234567890",
      "address": "123 Main St",
      "city": "New York",
      "state": "NY",
      "postal_code": "10001",
      "business_name": "Admin Business",
      "business_type": "Technology",
      "is_verified": true,
      "is_active": true,
      "is_staff": true,
      "is_superuser": true,
      "created_at": "2025-01-20T10:00:00Z",
      "updated_at": "2025-01-20T10:00:00Z"
    }
  ]
}
```

#### Create User
```http
POST /api/crud/users/
```

**Request Body:**
```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "first_name": "New",
  "last_name": "User",
  "role": "buyer",
  "user_type": "buyer",
  "password": "securepassword123",
  "phone": "+1234567890",
  "address": "456 Oak Ave",
  "city": "Los Angeles",
  "state": "CA",
  "postal_code": "90210"
}
```

#### Get User Detail
```http
GET /api/crud/users/{id}/
```

#### Update User
```http
PUT /api/crud/users/{id}/
PATCH /api/crud/users/{id}/
```

#### Delete User
```http
DELETE /api/crud/users/{id}/
```

---

## 🏢 **MASTER DATA MANAGEMENT**

### Companies

**Base Endpoint:** `/masters/companies/`

#### List Companies
```http
GET /api/crud/masters/companies/
```

**Query Parameters:**
- `is_active` - Filter by active status
- `search` - Search in name, email, phone, address

#### Create Company
```http
POST /api/crud/masters/companies/
```

**Request Body:**
```json
{
  "name": "Acme Corporation",
  "email": "contact@acme.com",
  "phone": "+1234567890",
  "address": "123 Business St",
  "city": "New York",
  "state": "NY",
  "postal_code": "10001",
  "website": "https://acme.com",
  "is_active": true
}
```

### Contacts

**Base Endpoint:** `/masters/contacts/`

#### List Contacts
```http
GET /api/crud/masters/contacts/
```

**Query Parameters:**
- `contact_type` - Filter by contact type (customer, supplier, vendor)
- `is_active` - Filter by active status
- `company` - Filter by company ID
- `search` - Search in name, email, phone, address

#### Create Contact
```http
POST /api/crud/masters/contacts/
```

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1234567890",
  "address": "123 Main St",
  "city": "New York",
  "state": "NY",
  "postal_code": "10001",
  "contact_type": "customer",
  "company": 1,
  "is_active": true
}
```

### Categories

**Base Endpoint:** `/masters/categories/`

#### List Categories
```http
GET /api/crud/masters/categories/
```

**Query Parameters:**
- `parent` - Filter by parent category ID
- `is_active` - Filter by active status
- `search` - Search in name, description

#### Create Category
```http
POST /api/crud/masters/categories/
```

**Request Body:**
```json
{
  "name": "Electronics",
  "description": "Electronic devices and accessories",
  "parent": null,
  "image": "path/to/image.jpg",
  "is_active": true
}
```

### Products

**Base Endpoint:** `/masters/products/`

#### List Products
```http
GET /api/crud/masters/products/
```

**Query Parameters:**
- `category` - Filter by category ID
- `subcategory` - Filter by subcategory ID
- `product_type` - Filter by product type (goods, service)
- `is_active` - Filter by active status
- `is_featured` - Filter by featured status
- `company` - Filter by company ID
- `search` - Search in name, description, sku, manufacturer

#### Create Product
```http
POST /api/crud/masters/products/
```

**Request Body:**
```json
{
  "company": 1,
  "category": 1,
  "subcategory": 2,
  "name": "Wireless Headphones",
  "description": "High-quality wireless headphones",
  "product_type": "goods",
  "sku": "WH-001",
  "unit_price": 99.99,
  "cost_price": 60.00,
  "tax": 1,
  "manufacturer": "TechBrand",
  "delivery_time": "3-5 days",
  "is_featured": true,
  "stock_quantity": 100,
  "min_order_quantity": 1,
  "is_active": true
}
```

### Product Images

**Base Endpoint:** `/masters/products/{product_id}/images/`

#### List Product Images
```http
GET /api/crud/masters/products/{product_id}/images/
```

#### Create Product Image
```http
POST /api/crud/masters/products/{product_id}/images/
```

**Request Body:**
```json
{
  "image": "path/to/product-image.jpg",
  "alt_text": "Product image description",
  "is_primary": true,
  "sort_order": 1
}
```

### Product Reviews

**Base Endpoint:** `/masters/products/{product_id}/reviews/`

#### List Product Reviews
```http
GET /api/crud/masters/products/{product_id}/reviews/
```

#### Create Product Review
```http
POST /api/crud/masters/products/{product_id}/reviews/
```

**Request Body:**
```json
{
  "rating": 5,
  "title": "Great product!",
  "comment": "Really happy with this purchase",
  "is_verified": true
}
```

### Taxes

**Base Endpoint:** `/masters/taxes/`

#### List Taxes
```http
GET /api/crud/masters/taxes/
```

#### Create Tax
```http
POST /api/crud/masters/taxes/
```

**Request Body:**
```json
{
  "name": "GST",
  "rate": 18.0,
  "description": "Goods and Services Tax",
  "is_active": true
}
```

### Chart of Accounts

**Base Endpoint:** `/masters/chart-of-accounts/`

#### List Chart of Accounts
```http
GET /api/crud/masters/chart-of-accounts/
```

#### Create Chart of Accounts
```http
POST /api/crud/masters/chart-of-accounts/
```

**Request Body:**
```json
{
  "name": "Cash",
  "code": "1000",
  "account_type": "asset",
  "description": "Cash in hand and bank",
  "parent": null,
  "is_active": true
}
```

---

## 🛒 **E-COMMERCE MANAGEMENT**

### Shopping Cart

**Base Endpoint:** `/ecommerce/carts/`

#### List Cart Items
```http
GET /api/crud/ecommerce/carts/
```

#### Add to Cart
```http
POST /api/crud/ecommerce/carts/
```

**Request Body:**
```json
{
  "product": 1,
  "quantity": 2
}
```

#### Update Cart Item
```http
PUT /api/crud/ecommerce/carts/{id}/
PATCH /api/crud/ecommerce/carts/{id}/
```

#### Remove from Cart
```http
DELETE /api/crud/ecommerce/carts/{id}/
```

### Orders

**Base Endpoint:** `/ecommerce/orders/`

#### List Orders
```http
GET /api/crud/ecommerce/orders/
```

**Query Parameters:**
- `status` - Filter by order status
- `payment_status` - Filter by payment status
- `search` - Search in order_number, shipping_address

#### Create Order
```http
POST /api/crud/ecommerce/orders/
```

**Request Body:**
```json
{
  "shipping_address": "123 Delivery St, City, State 12345",
  "payment_method": "credit_card",
  "notes": "Please deliver after 5 PM"
}
```

### Order Items

**Base Endpoint:** `/ecommerce/order-items/`

#### List Order Items
```http
GET /api/crud/ecommerce/order-items/
```

#### Create Order Item
```http
POST /api/crud/ecommerce/order-items/
```

**Request Body:**
```json
{
  "order": 1,
  "product": 1,
  "quantity": 2,
  "unit_price": 99.99
}
```

---

## 🏪 **SELLER MANAGEMENT**

### Seller Profiles

**Base Endpoint:** `/sellers/seller-profiles/`

#### List Seller Profiles
```http
GET /api/crud/sellers/seller-profiles/
```

#### Create Seller Profile
```http
POST /api/crud/sellers/seller-profiles/
```

**Request Body:**
```json
{
  "business_name": "My Store",
  "business_type": "retail",
  "description": "Quality products at great prices",
  "website": "https://mystore.com",
  "is_verified": false,
  "is_active": true
}
```

### Seller Products

**Base Endpoint:** `/sellers/seller-products/`

#### List Seller Products
```http
GET /api/crud/sellers/seller-products/
```

#### Create Seller Product
```http
POST /api/crud/sellers/seller-products/
```

**Request Body:**
```json
{
  "product": 1,
  "selling_price": 89.99,
  "commission_rate": 10.0,
  "is_approved": false,
  "is_active": true
}
```

### Seller Invoices

**Base Endpoint:** `/sellers/seller-invoices/`

#### List Seller Invoices
```http
GET /api/crud/sellers/seller-invoices/
```

#### Create Seller Invoice
```http
POST /api/crud/sellers/seller-invoices/
```

**Request Body:**
```json
{
  "seller": 1,
  "total_amount": 1000.00,
  "commission_amount": 100.00,
  "status": "pending",
  "is_paid": false
}
```

---

## 📦 **PURCHASE MANAGEMENT**

### Purchase Orders

**Base Endpoint:** `/purchases/purchase-orders/`

#### List Purchase Orders
```http
GET /api/crud/purchases/purchase-orders/
```

#### Create Purchase Order
```http
POST /api/crud/purchases/purchase-orders/
```

**Request Body:**
```json
{
  "supplier": 1,
  "order_date": "2025-01-20",
  "expected_delivery_date": "2025-01-25",
  "status": "pending",
  "notes": "Urgent delivery required"
}
```

---

## 💰 **SALES MANAGEMENT**

### Sales Orders

**Base Endpoint:** `/sales/sales-orders/`

#### List Sales Orders
```http
GET /api/crud/sales/sales-orders/
```

#### Create Sales Order
```http
POST /api/crud/sales/sales-orders/
```

**Request Body:**
```json
{
  "customer": 1,
  "order_date": "2025-01-20",
  "expected_delivery_date": "2025-01-25",
  "status": "pending",
  "notes": "Customer requested express delivery"
}
```

### Customer Invoices

**Base Endpoint:** `/sales/customer-invoices/`

#### List Customer Invoices
```http
GET /api/crud/sales/customer-invoices/
```

#### Create Customer Invoice
```http
POST /api/crud/sales/customer-invoices/
```

**Request Body:**
```json
{
  "customer": 1,
  "invoice_date": "2025-01-20",
  "due_date": "2025-02-20",
  "status": "pending",
  "is_paid": false,
  "payment_method": "credit_card"
}
```

---

## 📊 **INVENTORY MANAGEMENT**

### Stock Movements

**Base Endpoint:** `/inventory/stock-movements/`

#### List Stock Movements
```http
GET /api/crud/inventory/stock-movements/
```

#### Create Stock Movement
```http
POST /api/crud/inventory/stock-movements/
```

**Request Body:**
```json
{
  "product": 1,
  "movement_type": "in",
  "quantity": 100,
  "reference_type": "purchase_order",
  "reference_id": 1,
  "notes": "Stock received from supplier"
}
```

---

## 📈 **REPORTS & ANALYTICS**

### Sales Reports

**Base Endpoint:** `/reports/sales-reports/`

#### List Sales Reports
```http
GET /api/crud/reports/sales-reports/
```

#### Create Sales Report
```http
POST /api/crud/reports/sales-reports/
```

**Request Body:**
```json
{
  "report_name": "Monthly Sales Report",
  "report_type": "monthly",
  "start_date": "2025-01-01",
  "end_date": "2025-01-31"
}
```

### Product Analytics

**Base Endpoint:** `/reports/product-analytics/`

#### List Product Analytics
```http
GET /api/crud/reports/product-analytics/
```

#### Create Product Analytics
```http
POST /api/crud/reports/product-analytics/
```

**Request Body:**
```json
{
  "product": 1,
  "analytics_type": "daily",
  "analytics_date": "2025-01-20",
  "views_count": 150,
  "sales_count": 25,
  "revenue": 2499.75
}
```

---

## 🔄 **BULK OPERATIONS**

### Bulk Delete

**Endpoint:** `/bulk/delete/{model_name}/`

```http
POST /api/crud/bulk/delete/companies/
```

**Request Body:**
```json
{
  "ids": [1, 2, 3, 4, 5]
}
```

### Bulk Update

**Endpoint:** `/bulk/update/{model_name}/**

```http
POST /api/crud/bulk/update/companies/
```

**Request Body:**
```json
{
  "ids": [1, 2, 3],
  "update_data": {
    "is_active": false
  }
}
```

---

## 🚨 **ERROR HANDLING**

### Common Error Responses

#### 400 Bad Request
```json
{
  "field_name": ["This field is required."],
  "non_field_errors": ["Custom error message"]
}
```

#### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

#### 403 Forbidden
```json
{
  "detail": "You do not have permission to perform this action."
}
```

#### 404 Not Found
```json
{
  "detail": "Not found."
}
```

#### 500 Internal Server Error
```json
{
  "detail": "A server error occurred."
}
```

---

## 🧪 **TESTING**

### Test Script

Run the comprehensive CRUD test script:

```bash
python test_crud_operations.py
```

### Manual Testing

1. **Login** to get authentication token
2. **Create** records using POST endpoints
3. **List** records using GET endpoints
4. **Update** records using PUT/PATCH endpoints
5. **Delete** records using DELETE endpoints
6. **Test bulk operations** for multiple records

---

## 📝 **NOTES**

- All timestamps are in ISO 8601 format (UTC)
- All monetary values are in decimal format
- Image uploads require multipart/form-data content type
- Pagination is applied to all list endpoints
- Search functionality is available on most endpoints
- Filtering and ordering are supported on most endpoints
- All endpoints require proper authentication
- Rate limiting may apply to prevent abuse

---

## 🔗 **RELATED DOCUMENTATION**

- [Authentication API Documentation](AUTH_API_DOCUMENTATION.md)
- [E-commerce API Documentation](ECOMMERCE_API_DOCUMENTATION.md)
- [Reports API Documentation](REPORTS_API_DOCUMENTATION.md)
