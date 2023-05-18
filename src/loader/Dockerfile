FROM python:3.10.7-slim-bullseye

WORKDIR /app

COPY app/. .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -u Test.py
RUN rm Test.py
RUN rm .env

RUN mkdir temp-files

CMD ["python", "./__init__.py"]