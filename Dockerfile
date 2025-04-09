# Use the Python 3 alpine official image
# https://hub.docker.com/_/python
FROM python:3-alpine

# Create and change to the app directory.
WORKDIR /app

# Copy local code to the container image.
COPY . .

# Install system dependencies and project dependencies
RUN apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    linux-headers \
    make \
    && pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup.
CMD ["hypercorn", "main:app", "--bind", "::"]