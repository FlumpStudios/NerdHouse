@echo "starting server"
cd %~dp0
cls
start cmd /C python manage.py createsuperuser

