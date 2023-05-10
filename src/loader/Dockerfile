FROM python:3.10.7-slim-bullseye

EXPOSE 5000

WORKDIR /app

COPY app/. .
RUN pip3 install --no-cache-dir -r requirements.txt

#RUN python -u tests.py
#RUN rm .env

CMD ["python3", "./loader.py"]