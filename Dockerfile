# Use the official Python image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 5000

# Set environment variables for MongoDB connection from Docker environment
ENV MONGODB_USERNAME=${MONGODB_USERNAME}
ENV MONGODB_PASSWORD=${MONGODB_PASSWORD}
ENV AWS_DNS=${AWS_DNS}
ENV MONGODB_PORT=${MONGODB_PORT}
ENV MONGODB_NAME=${MONGODB_NAME}

# Command to run the application
CMD ["python", "app.py"]
