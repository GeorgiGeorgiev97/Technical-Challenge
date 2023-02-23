# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt api.py /app/

# Install any needed packages specified in requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Run app.py when the container launches
CMD [ "uvicorn", "api:app","--port","8000", "--reload"]