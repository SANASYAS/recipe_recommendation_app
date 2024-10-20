# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable (if needed)
ENV NAME RecipeApp

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
