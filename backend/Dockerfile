FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Set environment variables
ENV GOOGLE_CLOUD_PROJECT=jsgvlyff
ENV GOOGLE_CLOUD_LOCATION=us-central1

# Expose port
EXPOSE 8080

# Run ADK web server
CMD ["adk", "web", ".", "--port", "8080"]