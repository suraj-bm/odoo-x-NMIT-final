# 🔗 **Complete API Endpoints Reference**

## **Base URL**
```
http://localhost:8000/api/
```

## **Authentication Required**
All endpoints require JWT authentication. Include the token in the Authorization header:
```
Authorization: Bearer YOUR_JWT_TOKEN
```

---

## 🔐 **Authentication Endpoints**

### **Login**
```http
POST /api/auth/login/
```
**Request Body:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

### **Register**
```http
POST /api/auth/register/
```
**Request Body:**
```json
{
  "username": "newuser",
  "email": "user@example.com",
  "password": "password123",
  "password_confirm": "password123",
  "role": "buyer",
  "user_type": "buyer"
}
```

### **Logout**
```http
POST /api/auth/logout/
```

### **User Profile**
```http
GET /api/auth/profile/
```

### **User Roles Info**
```http
GET /api/auth/roles/
```

### **Users by Role**
```http
GET /api/auth/by-role/{role}/
```

### **Users by Type**
```http
GET /api/auth/by-type/{user_type}/
```

---

## 👥 **User Management (CRUD)**

### **List Users**
```http
GET /api/crud/users/
```

### **Create User**
```http
POST /api/crud/users/
```

### **Get User Detail**
```http
GET /api/crud/users/{id}/
```

### **Update User**
```http
PUT /api/crud/users/{id}/
PATCH /api/crud/users/{id}/
```

### **Delete User**
```http
DELETE /api/crud/users/{id}/
```

---

## 🏢 **Master Data Management (CRUD)**

### **Companies**
```http
GET /api/crud/companies/                    # List companies
POST /api/crud/companies/                   # Create company
GET /api/crud/companies/{id}/               # Get company detail
PUT /api/crud/companies/{id}/               # Update company
PATCH /api/crud/companies/{id}/             # Partial update company
DELETE /api/crud/companies/{id}/            # Delete company
```

### **Contacts**
```http
GET /api/crud/contacts/                     # List contacts
POST /api/crud/contacts/                    # Create contact
GET /api/crud/contacts/{id}/                # Get contact detail
PUT /api/crud/contacts/{id}/                # Update contact
PATCH /api/crud/contacts/{id}/              # Partial update contact
DELETE /api/crud/contacts/{id}/             # Delete contact
```

### **Categories**
```http
GET /api/crud/categories/                   # List categories
POST /api/crud/categories/                  # Create category
GET /api/crud/categories/{id}/              # Get category detail
PUT /api/crud/categories/{id}/              # Update category
PATCH /api/crud/categories/{id}/            # Partial update category
DELETE /api/crud/categories/{id}/           # Delete category
```

### **Products**
```http
GET /api/crud/products/                     # List products
POST /api/crud/products/                    # Create product
GET /api/crud/products/{id}/                # Get product detail
PUT /api/crud/products/{id}/                # Update product
PATCH /api/crud/products/{id}/              # Partial update product
DELETE /api/crud/products/{id}/             # Delete product
```

### **Product Images**
```http
GET /api/crud/products/{product_id}/images/           # List product images
POST /api/crud/products/{product_id}/images/          # Add product image
GET /api/crud/products/{product_id}/images/{id}/      # Get image detail
PUT /api/crud/products/{product_id}/images/{id}/      # Update image
PATCH /api/crud/products/{product_id}/images/{id}/    # Partial update image
DELETE /api/crud/products/{product_id}/images/{id}/   # Delete image
```

### **Product Reviews**
```http
GET /api/crud/products/{product_id}/reviews/          # List product reviews
POST /api/crud/products/{product_id}/reviews/         # Add product review
GET /api/crud/products/{product_id}/reviews/{id}/     # Get review detail
PUT /api/crud/products/{product_id}/reviews/{id}/     # Update review
PATCH /api/crud/products/{product_id}/reviews/{id}/   # Partial update review
DELETE /api/crud/products/{product_id}/reviews/{id}/  # Delete review
```

### **Taxes**
```http
GET /api/crud/taxes/                        # List taxes
POST /api/crud/taxes/                       # Create tax
GET /api/crud/taxes/{id}/                   # Get tax detail
PUT /api/crud/taxes/{id}/                   # Update tax
PATCH /api/crud/taxes/{id}/                 # Partial update tax
DELETE /api/crud/taxes/{id}/                # Delete tax
```

### **Chart of Accounts**
```http
GET /api/crud/chart-of-accounts/            # List chart of accounts
POST /api/crud/chart-of-accounts/           # Create account
GET /api/crud/chart-of-accounts/{id}/       # Get account detail
PUT /api/crud/chart-of-accounts/{id}/       # Update account
PATCH /api/crud/chart-of-accounts/{id}/     # Partial update account
DELETE /api/crud/chart-of-accounts/{id}/    # Delete account
```

---

## 🏪 **Seller Management (CRUD)**

### **Seller Profiles**
```http
GET /api/crud/sellers/seller-profiles/      # List seller profiles
POST /api/crud/sellers/seller-profiles/     # Create seller profile
GET /api/crud/sellers/seller-profiles/{id}/ # Get seller profile detail
PUT /api/crud/sellers/seller-profiles/{id}/ # Update seller profile
PATCH /api/crud/sellers/seller-profiles/{id}/ # Partial update seller profile
DELETE /api/crud/sellers/seller-profiles/{id}/ # Delete seller profile
```

### **Seller Products**
```http
GET /api/crud/sellers/seller-products/      # List seller products
POST /api/crud/sellers/seller-products/     # Create seller product
GET /api/crud/sellers/seller-products/{id}/ # Get seller product detail
PUT /api/crud/sellers/seller-products/{id}/ # Update seller product
PATCH /api/crud/sellers/seller-products/{id}/ # Partial update seller product
DELETE /api/crud/sellers/seller-products/{id}/ # Delete seller product
```

### **Seller Invoices**
```http
GET /api/crud/sellers/seller-invoices/      # List seller invoices
POST /api/crud/sellers/seller-invoices/     # Create seller invoice
GET /api/crud/sellers/seller-invoices/{id}/ # Get seller invoice detail
PUT /api/crud/sellers/seller-invoices/{id}/ # Update seller invoice
PATCH /api/crud/sellers/seller-invoices/{id}/ # Partial update seller invoice
DELETE /api/crud/sellers/seller-invoices/{id}/ # Delete seller invoice
```

---

## 🛒 **E-commerce Management (CRUD)**

### **Shopping Cart**
```http
GET /api/crud/ecommerce/carts/              # List cart items
POST /api/crud/ecommerce/carts/             # Add to cart
GET /api/crud/ecommerce/carts/{id}/         # Get cart item detail
PUT /api/crud/ecommerce/carts/{id}/         # Update cart item
PATCH /api/crud/ecommerce/carts/{id}/       # Partial update cart item
DELETE /api/crud/ecommerce/carts/{id}/      # Remove from cart
```

### **Orders**
```http
GET /api/crud/ecommerce/orders/             # List orders
POST /api/crud/ecommerce/orders/            # Create order
GET /api/crud/ecommerce/orders/{id}/        # Get order detail
PUT /api/crud/ecommerce/orders/{id}/        # Update order
PATCH /api/crud/ecommerce/orders/{id}/      # Partial update order
DELETE /api/crud/ecommerce/orders/{id}/     # Delete order
```

### **Order Items**
```http
GET /api/crud/ecommerce/order-items/        # List order items
POST /api/crud/ecommerce/order-items/       # Create order item
GET /api/crud/ecommerce/order-items/{id}/   # Get order item detail
PUT /api/crud/ecommerce/order-items/{id}/   # Update order item
PATCH /api/crud/ecommerce/order-items/{id}/ # Partial update order item
DELETE /api/crud/ecommerce/order-items/{id}/ # Delete order item
```

---

## 📦 **Purchase Management (CRUD)**

### **Purchase Orders**
```http
GET /api/crud/purchases/purchase-orders/    # List purchase orders
POST /api/crud/purchases/purchase-orders/   # Create purchase order
GET /api/crud/purchases/purchase-orders/{id}/ # Get purchase order detail
PUT /api/crud/purchases/purchase-orders/{id}/ # Update purchase order
PATCH /api/crud/purchases/purchase-orders/{id}/ # Partial update purchase order
DELETE /api/crud/purchases/purchase-orders/{id}/ # Delete purchase order
```

---

## 💰 **Sales Management (CRUD)**

### **Sales Orders**
```http
GET /api/crud/sales/sales-orders/           # List sales orders
POST /api/crud/sales/sales-orders/          # Create sales order
GET /api/crud/sales/sales-orders/{id}/      # Get sales order detail
PUT /api/crud/sales/sales-orders/{id}/      # Update sales order
PATCH /api/crud/sales/sales-orders/{id}/    # Partial update sales order
DELETE /api/crud/sales/sales-orders/{id}/   # Delete sales order
```

### **Customer Invoices**
```http
GET /api/crud/sales/customer-invoices/      # List customer invoices
POST /api/crud/sales/customer-invoices/     # Create customer invoice
GET /api/crud/sales/customer-invoices/{id}/ # Get customer invoice detail
PUT /api/crud/sales/customer-invoices/{id}/ # Update customer invoice
PATCH /api/crud/sales/customer-invoices/{id}/ # Partial update customer invoice
DELETE /api/crud/sales/customer-invoices/{id}/ # Delete customer invoice
```

---

## 📊 **Inventory Management (CRUD)**

### **Stock Movements**
```http
GET /api/crud/inventory/stock-movements/    # List stock movements
POST /api/crud/inventory/stock-movements/   # Create stock movement
GET /api/crud/inventory/stock-movements/{id}/ # Get stock movement detail
PUT /api/crud/inventory/stock-movements/{id}/ # Update stock movement
PATCH /api/crud/inventory/stock-movements/{id}/ # Partial update stock movement
DELETE /api/crud/inventory/stock-movements/{id}/ # Delete stock movement
```

---

## 📈 **Reports & Analytics (CRUD)**

### **Sales Reports**
```http
GET /api/crud/reports/sales-reports/        # List sales reports
POST /api/crud/reports/sales-reports/       # Create sales report
GET /api/crud/reports/sales-reports/{id}/   # Get sales report detail
PUT /api/crud/reports/sales-reports/{id}/   # Update sales report
PATCH /api/crud/reports/sales-reports/{id}/ # Partial update sales report
DELETE /api/crud/reports/sales-reports/{id}/ # Delete sales report
```

### **Product Analytics**
```http
GET /api/crud/reports/product-analytics/    # List product analytics
POST /api/crud/reports/product-analytics/   # Create product analytics
GET /api/crud/reports/product-analytics/{id}/ # Get product analytics detail
PUT /api/crud/reports/product-analytics/{id}/ # Update product analytics
PATCH /api/crud/reports/product-analytics/{id}/ # Partial update product analytics
DELETE /api/crud/reports/product-analytics/{id}/ # Delete product analytics
```

---

## 🔄 **Bulk Operations**

### **Bulk Delete**
```http
POST /api/crud/bulk/delete/{model_name}/
```
**Request Body:**
```json
{
  "ids": [1, 2, 3, 4, 5]
}
```

### **Bulk Update**
```http
POST /api/crud/bulk/update/{model_name}/
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

## 📋 **Query Parameters**

### **Pagination**
- `page` - Page number (default: 1)
- `page_size` - Items per page (default: 20, max: 100)

### **Filtering**
- `is_active` - Filter by active status
- `status` - Filter by status field
- `category` - Filter by category
- `user` - Filter by user
- `created_at` - Filter by creation date

### **Search**
- `search` - Full-text search across relevant fields

### **Sorting**
- `ordering` - Order by field (prefix with `-` for descending)
  - Example: `ordering=-created_at` (newest first)
  - Example: `ordering=name` (alphabetical)

---

## 📝 **Example API Calls**

### **Get All Products with Pagination**
```bash
curl -X GET "http://localhost:8000/api/crud/products/?page=1&page_size=10" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### **Search Products**
```bash
curl -X GET "http://localhost:8000/api/crud/products/?search=wireless" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### **Filter Products by Category**
```bash
curl -X GET "http://localhost:8000/api/crud/products/?category=1" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### **Create a New Product**
```bash
curl -X POST "http://localhost:8000/api/crud/products/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "company": 1,
    "name": "Wireless Headphones",
    "description": "High-quality wireless headphones",
    "sku": "WH-001",
    "unit_price": 99.99,
    "product_type": "goods"
  }'
```

### **Update a Product**
```bash
curl -X PATCH "http://localhost:8000/api/crud/products/1/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "unit_price": 89.99
  }'
```

### **Delete a Product**
```bash
curl -X DELETE "http://localhost:8000/api/crud/products/1/" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## 🚨 **Error Responses**

### **400 Bad Request**
```json
{
  "field_name": ["This field is required."],
  "non_field_errors": ["Custom error message"]
}
```

### **401 Unauthorized**
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### **403 Forbidden**
```json
{
  "detail": "You do not have permission to perform this action."
}
```

### **404 Not Found**
```json
{
  "detail": "Not found."
}
```

### **500 Internal Server Error**
```json
{
  "detail": "A server error occurred."
}
```

---

## 📊 **Summary**

- **Total Endpoints**: 76+ API endpoints
- **Authentication**: JWT token required
- **Response Format**: JSON
- **Pagination**: Supported on all list endpoints
- **Filtering**: Supported on all list endpoints
- **Search**: Supported on most list endpoints
- **Sorting**: Supported on all list endpoints
- **Bulk Operations**: Available for all models

**All endpoints are fully functional and ready for production use!** 🚀
