# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# COPY requirements.txt .
COPY . .

# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir flask-swagger-ui

# COPY api.py .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
# ENV FLASK_APP=api.py

# Run app.py when the container launches
## CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["python", "api.py"]

# Adapted using Claude AI