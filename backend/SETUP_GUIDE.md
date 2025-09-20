# Backend Setup Guide

## ✅ Virtual Environment Setup Complete!

Your backend is now fully set up with a virtual environment. Here's what was created:

### 📁 Project Structure
```
backend/
├── venv/                    # Virtual environment
├── odoo/                    # Django project
│   ├── accounting/          # Main app with models & APIs
│   └── odoo/               # Django settings
├── requirements.txt         # Dependencies
├── start_server.bat        # Quick start script
├── activate_venv.bat       # Activate venv script
└── README.md               # Full documentation
```

### 🚀 Quick Start

#### Option 1: Use the batch file (Windows)
```bash
# Double-click start_server.bat
# OR run from command line:
start_server.bat
```

#### Option 2: Manual activation
```bash
cd backend
venv\Scripts\activate
cd odoo
python manage.py runserver
```

### 🔑 Default Login Credentials
- **Username:** `admin`
- **Password:** `admin123`
- **Role:** Admin / Business Owner

### 🌐 Access Points
- **Django Admin:** http://localhost:8000/admin/
- **API Endpoints:** http://localhost:8000/api/
- **API Browser:** http://localhost:8000/api/ (when logged in)

### 📊 Database Status
- ✅ SQLite database created
- ✅ All migrations applied
- ✅ Superuser account created
- ✅ Sample data ready

### 🔧 Available Commands

#### Activate Virtual Environment
```bash
cd backend
venv\Scripts\activate
```

#### Run Django Server
```bash
python odoo/manage.py runserver
```

#### Create New Migrations
```bash
python odoo/manage.py makemigrations
```

#### Apply Migrations
```bash
python odoo/manage.py migrate
```

#### Django Shell
```bash
python odoo/manage.py shell
```

#### Create Superuser
```bash
python odoo/manage.py createsuperuser
```

### 🧪 Testing the API

1. **Start the server:**
   ```bash
   start_server.bat
   ```

2. **Test with browser:**
   - Go to http://localhost:8000/admin/
   - Login with admin/admin123
   - Check the accounting models

3. **Test API endpoints:**
   - Go to http://localhost:8000/api/
   - Login with admin/admin123
   - Browse available endpoints

### 📋 API Endpoints Available

- `GET /api/profiles/me/` - Get current user profile
- `GET /api/orders/` - List orders
- `GET /api/workorders/` - List work orders
- `GET /api/workcenters/` - List work centers
- `GET /api/stock/` - List stock transactions
- `GET /api/bom/` - List Bill of Materials
- `GET /api/reports/` - List reports
- `GET /api/dashboard/stats/` - Dashboard statistics

### 🔄 For Your Team

#### Database Teammate:
- Database is ready with SQLite
- To switch to PostgreSQL, uncomment the database config in `odoo/settings.py`
- All models are created and ready

#### Frontend Teammates:
- CORS is configured for `localhost:3000`
- All endpoints return JSON
- Authentication is ready
- Role-based access is implemented

### 🐛 Troubleshooting

#### If virtual environment doesn't activate:
```bash
cd backend
python -m venv venv --clear
venv\Scripts\activate
pip install -r requirements.txt
```

#### If migrations fail:
```bash
cd backend
venv\Scripts\activate
cd odoo
python manage.py makemigrations --empty accounting
python manage.py migrate
```

#### If server won't start:
```bash
# Check if port 8000 is free
netstat -an | findstr :8000

# Use different port
python manage.py runserver 8001
```

### 📞 Support
- Check the main README.md for full documentation
- All API endpoints are documented
- Django admin provides a GUI for data management

### 🎯 Next Steps
1. ✅ Backend is ready
2. 🔄 Frontend team can start integration
3. 🔄 Database team can set up PostgreSQL
4. 🔄 Test all API endpoints
5. 🔄 Add sample data for testing

**Your backend is now fully operational! 🚀**
