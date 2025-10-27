# course-catalogue/Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

COPY . . 

# Ensure script is executable by running wait for it file to check for availability
RUN chmod +x /app/wait-for-it.sh

EXPOSE 5002

# Wait for course-db before starting Flask (more logical command order)
CMD ["./wait-for-it.sh", "course-db", "5432", "python", "app.py"]