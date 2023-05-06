docker login

@echo off
set /p "username=Enter your docker username = "

docker build -t %username%/react-app:latest .
docker push %username%/react-app:latest