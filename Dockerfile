# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install pytest
RUN pip install pytest

# Run main.py by default
CMD ["python", "main.py"]
