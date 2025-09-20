@echo off
echo Starting Manufacturing Management System Backend...
echo.
echo Virtual Environment: backend/venv
echo Django Server: http://localhost:8000
echo Admin Panel: http://localhost:8000/admin
echo API Endpoints: http://localhost:8000/api/
echo.
echo Default Login:
echo Username: admin
echo Password: admin123
echo.
echo Press Ctrl+C to stop the server
echo.

cd /d "%~dp0"
call venv\Scripts\activate
cd odoo
python manage.py runserver
