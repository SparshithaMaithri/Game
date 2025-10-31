FROM python:3.9-slim-buster

WORKDIR /app

# copy only what's needed first for cache efficiency
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

# Use gunicorn for containers (better than flask dev server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2", "--timeout", "120"]
