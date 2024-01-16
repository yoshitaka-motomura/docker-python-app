FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy all files from src to /app
COPY ./src .

ENV FLASK_APP=app.py

# Healthcheck
HEALTHCHECK --interval=5s --timeout=3s \
  CMD curl -f http://0.0.0.0:8000/health || exit 1

## Expose port because gunicorn is running on this port
EXPOSE 8000

# guicorn is a production ready server
CMD ["gunicorn","-w 2" ,"-b", "0.0.0.0", "app:app"]
