# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install required packages
RUN pip install fastapi uvicorn pytest httpx

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your FastAPI app and python tests
COPY ./app ./app
COPY ./tests ./tests

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the server
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Run the server with Live Reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

