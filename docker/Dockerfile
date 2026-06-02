# docker/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY src/ ./src
COPY models/ ./models
COPY app.py .

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
