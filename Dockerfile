# Use a newer Python version
FROM python:3.11-slim

WORKDIR /app

# Upgrade pip first to ensure it can find the latest packages
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]