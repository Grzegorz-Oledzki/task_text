# Use the official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /text_task

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Copy the application code
COPY . .
CMD ["python", "./text_task/manage.py", "runserver", "0.0.0.0:8000"]