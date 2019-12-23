@echo "starting server"
cd %~dp0
start cmd /k python manage.py runserver 8003
PING localhost -n 6 >NUL
start "" http://localhost:8003/admin