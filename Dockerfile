FROM python:3.11-slim

WORKDIR /code

# Install system dependencies for PostgreSQL (if needed)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /code/

EXPOSE ${DJANGO_PORT}

# Run migrations and start Gunicorn
CMD ["sh", "-c", "ls -R /code && python manage.py migrate && gunicorn --bind ${DJANGO_HOST}:${DJANGO_PORT} catmed.wsgi:application"]
