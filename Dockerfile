# Use the official Python image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files into container
COPY my-static-site /app/

# Set Django settings environment variable
ENV DJANGO_SETTINGS_MODULE=band_site.settings

# Run migrations and start the development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
