FROM python:3.12-slim-bookworm

ARG IP_ADDRESS
ENV IP_ADDRESS=${IP_ADDRESS}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

# If you want to use pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code

RUN python manage.py collectstatic --noinput

RUN chmod +x /code/entrypoint.sh