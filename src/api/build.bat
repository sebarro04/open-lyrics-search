docker login

@echo off
set /p "username=Enter your docker username = "

docker build -t %username%/api-open-lyrics-search:latest .
docker push %username%/api-open-lyrics-search:latest