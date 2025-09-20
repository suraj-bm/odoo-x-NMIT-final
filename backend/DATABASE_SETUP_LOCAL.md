# Local Database Setup Guide

## 🎯 **For Database Teammate**

Since we can't use online services, we'll set up PostgreSQL locally on your machine.

---

## 📥 **Step 1: Install PostgreSQL**

### Windows Installation:
1. **Download PostgreSQL:**
   - Go to: https://www.postgresql.org/download/windows/
   - Download the latest version (15.x or 16.x)
   - Choose the installer for your Windows version

2. **Install PostgreSQL:**
   - Run the installer as Administrator
   - Choose installation directory (default is fine)
   - **IMPORTANT:** Remember the password you set for `postgres` user
   - Port: 5432 (default)
   - Locale: Default

3. **Verify Installation:**
   - Open Command Prompt
   - Run: `psql --version`
   - Should show PostgreSQL version

---

## 🗄️ **Step 2: Create Database**

### Using pgAdmin (GUI):
1. **Open pgAdmin:**
   - Find "pgAdmin 4" in Start Menu
   - Open and connect to PostgreSQL server

2. **Create Database:**
   - Right-click "Databases" → "Create" → "Database"
   - Name: `manufacturing_db`
   - Owner: `postgres`
   - Click "Save"

### Using Command Line:
```sql
-- Open Command Prompt and run:
psql -U postgres

-- Then run these SQL commands:
CREATE DATABASE manufacturing_db;
CREATE USER manufacturing_user WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE manufacturing_db TO manufacturing_user;
\q
```

---

## ⚙️ **Step 3: Update Django Settings**

1. **Open:** `backend/odoo/odoo/settings.py`

2. **Find the database section and replace:**
```python
# Replace this:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# With this:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'manufacturing_db',
        'USER': 'postgres',  # or 'manufacturing_user'
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. **Save the file**

---

## 🔄 **Step 4: Migrate Database**

1. **Open Command Prompt in backend directory:**
```bash
cd E:\ODOO\oddo-final\odoo-x-NMIT-final\backend
venv\Scripts\activate
cd odoo
```

2. **Run migrations:**
```bash
python manage.py migrate
```

3. **Create superuser:**
```bash
python manage.py createsuperuser
```

4. **Test connection:**
```bash
python manage.py runserver
```

---

## 🧪 **Step 5: Test Database**

1. **Start Django server:**
```bash
python manage.py runserver
```

2. **Open browser:**
   - Go to: http://localhost:8000/admin/
   - Login with your superuser credentials
   - Check if all tables are created

3. **Test API:**
   - Go to: http://localhost:8000/api/
   - Login and browse endpoints

---

## 📊 **Step 6: Add Sample Data**

Create a management command to populate sample data:

1. **Create management command:**
```bash
mkdir odoo\accounting\management
mkdir odoo\accounting\management\commands
```

2. **Create file:** `odoo\accounting\management\__init__.py` (empty file)

3. **Create file:** `odoo\accounting\management\commands\__init__.py` (empty file)

4. **Create file:** `odoo\accounting\management\commands\populate_data.py`

---

## 🔧 **Troubleshooting**

### Common Issues:

1. **"psql is not recognized":**
   - Add PostgreSQL bin directory to PATH
   - Or use full path: `C:\Program Files\PostgreSQL\16\bin\psql.exe`

2. **Connection refused:**
   - Check if PostgreSQL service is running
   - Windows Services → PostgreSQL → Start

3. **Authentication failed:**
   - Check username/password
   - Try connecting with pgAdmin first

4. **Database doesn't exist:**
   - Create database manually
   - Check database name in settings.py

### Useful Commands:

```bash
# Check PostgreSQL status
sc query postgresql-x64-16

# Start PostgreSQL service
net start postgresql-x64-16

# Stop PostgreSQL service
net stop postgresql-x64-16

# Connect to database
psql -U postgres -d manufacturing_db
```

---

## 📋 **Checklist**

- [ ] PostgreSQL installed
- [ ] Database `manufacturing_db` created
- [ ] User `manufacturing_user` created (optional)
- [ ] Django settings updated
- [ ] Migrations run successfully
- [ ] Superuser created
- [ ] Server starts without errors
- [ ] Admin panel accessible
- [ ] API endpoints working

---

## 🎯 **Next Steps After Database Setup**

1. **Test all API endpoints**
2. **Create sample data**
3. **Coordinate with frontend team**
4. **Set up database backups**
5. **Optimize database performance**

---

## 📞 **Support**

- **PostgreSQL Docs:** https://www.postgresql.org/docs/
- **Django Database Docs:** https://docs.djangoproject.com/en/5.2/ref/databases/
- **Backend Developer:** Contact for Django issues
- **Project README:** `backend/README.md`

**Your database setup is crucial for the project! Take your time and test thoroughly. 🚀**
