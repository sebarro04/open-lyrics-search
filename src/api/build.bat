docker login

@echo off
set /p "username=Enter your docker username = "

docker build -t %username%/api-songsearch:latest .
docker push %username%/api-songsearch:latest