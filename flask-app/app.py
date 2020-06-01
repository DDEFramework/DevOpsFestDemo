from flask import Flask
import os
from minio import Minio
from minio.error import ResponseError


minioClient = Minio('minio.default.svc.cluster.local',
                  access_key=os.environ.get('MINIO_ACCES_KEY'),
                  secret_key=os.environ.get('MINIO_SECRET_KEY'),
                  secure=True)


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/minio/list-buckets')
def minio_list_buckets():
    buckets = minioClient.list_buckets()

    buckets_info = list()

    for bucket in buckets:
        buckets_info.append(f'{bucket.name}, {bucket.creation_date}')
    return buckets_info