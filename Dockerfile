# Use the pre-built tiangolo/uvicorn-gunicorn-fastapi image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

LABEL authors="emmanuel"

# Set working directory and copy necessary files
WORKDIR /app
COPY main.py models.py requirements.txt ./

# Install Python packages from requirements.txt
RUN pip install -r requirements.txt

# Define the port number the container should expose
EXPOSE 8000

# Run the Uvicorn server with Gunicorn when the container starts
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]
