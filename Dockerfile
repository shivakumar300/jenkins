# Use official Python slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the dashboard.py file
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir dash pandas plotly numpy

# Expose port 8000
EXPOSE 8000
# Change
# Command to run the Dash app
CMD ["python", "app.py"]
