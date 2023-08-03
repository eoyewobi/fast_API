# Use the pre-built tiangolo/uvicorn-gunicorn-fastapi image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

LABEL authors="Emmanuel"

# Set working directory and copy necessary files
WORKDIR /app
COPY main.py models.py requirements.txt ./

# venv
ENV VIRTUAL_ENV=/home/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python packages from requirements.txt
RUN pip install -r requirements.txt

# Add a non-root user with UID 1000
RUN useradd --uid 1000 myuser
RUN mkdir -p /home/myuser
RUN chown -R myuser:myuser /home/myuser
USER myuser

# Define the port number the container should expose
EXPOSE 8000

# Run the Uvicorn server with Gunicorn when the container starts
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
