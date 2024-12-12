from flask import Flask, request
from minio import Minio
from minio.error import S3Error

app=Flask(__name__)


def get_client():
    
    url = input("Enter the S3 URL (e.g., localhost:9000): ")
    access_key = input("Enter the Access Key: ")
    secret_key = input("Enter the Secret Key: ")
    bucket_name = input("Enter the Bucket Name: ")

    
    client = Minio(url, access_key=access_key, secret_key=secret_key, secure=False)

  
    if not client.bucket_exists(bucket_name):
        print(f"Bucket '{bucket_name}' does not exist. Please create it in MinIO.")
        exit(1)
    
    return client, bucket_name


@app.route('/upload', methods=["POST"])
def upload_file(client, bucket_name):
    file_path = input("Enter the path of the file to upload: ")
    object_name = input("Enter the object name to store in S3: ")
    
    try:
        client.fput_object(bucket_name, object_name, file_path)
        print(f"'{file_path}' has been uploaded as '{object_name}'.")
    except S3Error as e:
        print("Error during upload:", e)

@app.route('/download')
def download_file(client, bucket_name):
    object_name = input("Enter the object name to download: ")
    download_path = input("Enter the download destination path: ")
    
    try:
        client.fget_object(bucket_name, object_name, download_path)
        print(f"'{object_name}' has been downloaded to '{download_path}'.")
    except S3Error as e:
        print("Error during download:", e)

@app.route('/list')
def list_files(client, bucket_name):
    try:
        objects = client.list_objects(bucket_name)
        print("Files in the bucket:")
        for obj in objects:
            print(f"- {obj.object_name}")
    except S3Error as e:
        print("Error listing files:", e)


if __name__ == "__main__":
    app.run(debug=True)
