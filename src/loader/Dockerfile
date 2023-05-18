FROM python:3.10.7-slim-bullseye

EXPOSE 5000

WORKDIR /app

COPY app/. .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -u Test.py
RUN rm Test.py
RUN rm .env

CMD ["python3", "./__init__.py"]