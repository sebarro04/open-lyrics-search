FROM python:3.11.3-slim-bullseye

EXPOSE 5000

WORKDIR /app

COPY app/. .
RUN pip install --no-cache-dir -r requirements.txt

RUN rm .env

CMD ["python", "-u", "__init__.py"]
