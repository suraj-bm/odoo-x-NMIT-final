# Manufacturing Management System - Backend

This is the Django REST API backend for the Manufacturing Management System hackathon project.

## Architecture Overview

The backend implements the following services as per the architecture diagram:

- **Auth Service** (`/api/auth/`) - User authentication and session management
- **Profile Service** (`/api/profiles/`) - User profile management with role-based access
- **Order Service** (`/api/orders/`) - Order management and work order creation
- **Work Order Service** (`/api/workorders/`) - Work order lifecycle management
- **Work Center Service** (`/api/workcenters/`) - Work center management and efficiency tracking
- **Stock Service** (`/api/stock/`) - Inventory management and stock ledger
- **BoM Service** (`/api/bom/`) - Bill of Materials management
- **Report Service** (`/api/reports/`) - Report generation and analytics
- **Dashboard Service** (`/api/dashboard/`) - Dashboard statistics and metrics

## User Roles

The system supports 4 user roles:
- **Manufacturing Manager** - Full access to all modules
- **Operator/Worker** - Limited access to assigned work orders
- **Inventory Manager** - Access to stock and inventory management
- **Admin/Business Owner** - Full system access

## Setup Instructions

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Database Setup

The system is configured to use SQLite by default for development. For production, uncomment the PostgreSQL configuration in `odoo/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'manufacturing_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Run Migrations

```bash
cd odoo
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## API Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout

### Profiles
- `GET /api/profiles/me/` - Get current user profile
- `PUT /api/profiles/me/` - Update current user profile

### Orders
- `GET /api/orders/` - List orders (filtered by role)
- `POST /api/orders/` - Create new order
- `GET /api/orders/{id}/` - Get order details
- `PUT /api/orders/{id}/` - Update order
- `POST /api/orders/{id}/create_work_order/` - Create work order for order

### Work Orders
- `GET /api/workorders/` - List work orders (filtered by role)
- `POST /api/workorders/` - Create work order
- `GET /api/workorders/{id}/` - Get work order details
- `POST /api/workorders/{id}/start_work/` - Start work on order
- `POST /api/workorders/{id}/complete_work/` - Complete work order

### Work Centers
- `GET /api/workcenters/` - List work centers
- `POST /api/workcenters/` - Create work center
- `GET /api/workcenters/{id}/efficiency/` - Get work center efficiency data

### Stock Management
- `GET /api/stock/` - List stock transactions
- `POST /api/stock/` - Create stock transaction
- `GET /api/stock/inventory_summary/` - Get inventory summary

### Bill of Materials
- `GET /api/bom/` - List BoMs
- `POST /api/bom/` - Create BoM
- `POST /api/bom/{id}/add_item/` - Add item to BoM

### Reports
- `GET /api/reports/` - List reports
- `GET /api/reports/generate_production_report/` - Generate production report

### Dashboard
- `GET /api/dashboard/stats/` - Get dashboard statistics

## Database Models

### Core Models
- **UserProfile** - Extended user information with roles
- **WorkCenter** - Manufacturing work centers
- **Order** - Customer orders
- **WorkOrder** - Manufacturing work orders
- **BillOfMaterials** - Product BoMs
- **BoMItem** - BoM components
- **StockLedger** - Inventory transactions
- **Report** - Generated reports

## Role-Based Access Control

The system implements role-based access control:

- **Manufacturing Manager**: Full access to all modules
- **Operator/Worker**: Access to assigned work orders only
- **Inventory Manager**: Access to stock and inventory management
- **Admin/Business Owner**: Full system access

## CORS Configuration

The backend is configured to accept requests from:
- `http://localhost:3000` (Next.js frontend)
- `http://127.0.0.1:3000`

## For Your Database Teammate

The system is ready for PostgreSQL integration. Simply:

1. Install PostgreSQL
2. Create a database named `manufacturing_db`
3. Uncomment the PostgreSQL configuration in `settings.py`
4. Update the database credentials
5. Run migrations

## For Your Frontend Teammates

The API is fully documented and ready for integration. All endpoints return JSON responses and support:

- Pagination (20 items per page)
- Filtering and searching
- Role-based data filtering
- RESTful conventions

## Testing the API

You can test the API using:

1. **Django Admin**: `http://localhost:8000/admin/`
2. **API Browser**: `http://localhost:8000/api/` (when logged in)
3. **Postman/Insomnia**: Use the endpoints listed above

## Next Steps

1. Set up the database (SQLite for development, PostgreSQL for production)
2. Create initial data using Django admin
3. Test all API endpoints
4. Coordinate with frontend team for integration
5. Implement additional business logic as needed

## Support

For questions or issues, refer to the Django REST Framework documentation or contact the backend team lead.
