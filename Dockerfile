# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory inside the container.
WORKDIR /app

# Install system dependencies required by Python and Pillow.
RUN apt-get update && apt-get install -y \
    build-essential libjpeg-dev zlib1g-dev libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies.
COPY requirements.txt .
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the static directory exists.
RUN mkdir -p /app/staticfiles

# Copy application code to the container.
COPY . .

# Collect static files for production use.
RUN python manage.py collectstatic --noinput

# Service must listen to $PORT environment variable.
ENV PORT 8080

# Ensure Python prints directly to the console without buffering.
ENV PYTHONUNBUFFERED TRUE

# Copy and set entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]
