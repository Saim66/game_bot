# Use an official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy your files
COPY . .

# Install the bot SDK
RUN pip install highrise-bot-sdk

# Start the bot
CMD ["python", "main.py"]