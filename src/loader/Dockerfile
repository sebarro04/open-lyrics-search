FROM python:3.10.7-slim-bullseye

WORKDIR /app

COPY app/. .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -u TestDataLoader.py
RUN rm TestDataLoader.py
RUN rm temp-files/*
RUN rm .env

#RUN mkdir temp-files

CMD ["python", "-u", "__init__.py"]