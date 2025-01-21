# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app
COPY _build/html/ /app/_build/html/

# Install Flask
RUN pip install flask

# Expose the Flask default port
EXPOSE 5000

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
