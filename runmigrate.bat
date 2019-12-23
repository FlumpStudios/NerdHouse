@echo "Running migrations"
cd %~dp0
python manage.py makemigrations
python manage.py migrate
