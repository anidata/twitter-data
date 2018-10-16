# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /search
WORKDIR /app

# Copy the current directory contents into the container at /search
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run search.py when the container launches
CMD ["python", "app.py"]