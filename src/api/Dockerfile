FROM python:3.10.7-slim-bullseye

EXPOSE 5000

WORKDIR /app

COPY app/. .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "./__init__.py"]
