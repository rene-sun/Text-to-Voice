# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install dependencies (including TTS models or other necessary packages)
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies (like espeak-ng)
RUN apt-get update && apt-get install -y espeak-ng ffmpeg libsndfile1

# Copy the rest of the application code into the container
COPY . .

# Expose the port (Render will use the PORT environment variable)
EXPOSE 8080

# Set environment variables (optional, like your API keys)
ENV TEXT-TO-VOICE-SECRET-KEY="8ef086c4fa9cc3bb3e00ba8b94a5a2e0"

# Command to run the application
CMD ["python", "app.py"]
