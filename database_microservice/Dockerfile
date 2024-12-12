
FROM python:3.11-slim


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir flask minio


EXPOSE 5003



CMD ["python", "-m", "database.minio"]
