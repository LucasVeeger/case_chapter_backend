# Use the Python 3.9 slim image which has better compatibility with ML libraries
FROM python:3.9-slim

# Create and change to the app directory.
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install system dependencies required for some Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install project dependencies
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the web service on container startup.
CMD ["hypercorn", "app/main.py", "--bind", "::"]