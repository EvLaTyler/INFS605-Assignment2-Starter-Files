# course-feedback/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

COPY . .

# Make wait-for-it.sh executable
RUN chmod +x /app/wait-for-it.sh

EXPOSE 5003

CMD ["./wait-for-it.sh", "python", "app.py"]
