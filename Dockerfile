# Use the official Python image as base
FROM python:3.8

# Set the working directory in the container
WORKDIR /bot

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python3", "bot.py"]
