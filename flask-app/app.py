from flask import Flask
import os
from minio import Minio
from minio.error import ResponseError


minioClient = Minio(f'{os.environ.get("MINIO_URL")}:9000',
                  access_key=os.environ.get('MINIO_ACCES_KEY'),
                  secret_key=os.environ.get('MINIO_SECRET_KEY'),
                  secure=True)


app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/minio/list-buckets')
def minio_list_buckets():
    buckets = minioClient.list_buckets()

    buckets_info = list()

    for bucket in buckets:
        buckets_info.append(f'{bucket.name}, {bucket.creation_date}')
    return buckets_info