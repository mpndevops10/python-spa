# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Copy the logo image to the static folder in the container
COPY IMG-2439.jpg /app/static/IMG-2439.jpg

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
