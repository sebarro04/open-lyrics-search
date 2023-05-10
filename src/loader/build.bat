docker login

@echo off
set /p "username=Enter your docker username = "

docker build -t %username%/loader:latest .
docker push %username%/loader:latest