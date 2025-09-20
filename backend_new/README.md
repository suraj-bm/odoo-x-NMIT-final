# Shiv Accounts Backend

A Django REST API backend for user management with role-based authentication.

## Features

- **User Management**: Custom User model with three roles (Admin, InvoicingUser, ContactUser)
- **JWT Authentication**: Secure token-based authentication using SimpleJWT
- **REST API**: Built with Django REST Framework

## User Roles

- **Admin**: Full system access
- **InvoicingUser**: Access to invoicing features
- **ContactUser**: Access to contact management features

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and get JWT tokens
- `POST /api/auth/logout/` - Logout and blacklist refresh token
- `GET /api/auth/profile/` - Get current user profile

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Create admin user:
   ```bash
   python manage.py seed_admin
   ```

4. Start development server:
   ```bash
   python manage.py runserver
   ```

## Default Admin User

- Username: `admin`
- Password: `admin123`
- Role: `admin`

## API Usage

### Register User
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password_confirm": "testpass123",
    "role": "contact_user"
  }'
```

### Login
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'
```

### Access Protected Endpoints
```bash
curl -X GET http://localhost:8000/api/auth/profile/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
