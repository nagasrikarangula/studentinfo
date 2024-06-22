# Use the official Python image from the Docker Hub
FROM python:3.8-slim
# Set the working directory
WORKDIR /app
# Copy the requirements file into the image
COPY requirements.txt requirements.txt
# Install the dependencies
RUN pip install -r requirements.txt
# Copy the rest of the application code into the image
COPY . .
# Run database initialization script
RUN python db.py
# Expose the port the app runs on
EXPOSE 5000
# Define the command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
