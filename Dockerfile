FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["uwsgi", "--http", ":8000", "--module", "bio.wsgi:application", "--static-map", "/static=/app/static", "--static-map", "/media=/app/media"] 