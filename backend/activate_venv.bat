@echo off
echo Activating virtual environment...
cd /d "%~dp0"
call venv\Scripts\activate
echo Virtual environment activated!
echo You can now run Django commands like:
echo   python odoo/manage.py runserver
echo   python odoo/manage.py shell
echo   python odoo/manage.py makemigrations
echo   python odoo/manage.py migrate
cmd /k
