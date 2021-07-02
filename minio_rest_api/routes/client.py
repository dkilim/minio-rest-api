from logging import exception
from fastapi import APIRouter
from minio_rest_api.config.client import client
from minio_rest_api.model.file import Delete, Download, Upload 

# create bucket functio
cl=APIRouter()
def create_mbucket(name:str):
    client.make_bucket(name)

# get all buckets from minio
@cl.get('/get-all-buckets')
def get_all_buckets():
    buckets=client.list_buckets()
    return buckets

# post request for create bucket
@cl.post('/create-bucket/{name}')
def create_bucket(name):
    if client.bucket_exists(name):
        print("name: {name}")
        return "Bucket is exist."
    else:
        create_mbucket(name)

#delete bucket
@cl.delete('/delete/{name}')
def delete_bucket(name):
    client.remove_bucket(name)

@cl.post('/upload')
def upload_file(bc: Upload):

    if client.bucket_exists(bc.bucket_name):                
        client.fput_object(bc.bucket_name, bc.object_name,bc.file_path)
    else:
        create_mbucket(bc.bucket_name)
        client.fput_object(bc.bucket_name, bc.object_name,bc.file_path)

@cl.get('/download')
def download_file(d: Download):
    test=client.fget_object(d.bucket_name, d.object_name, d.file_path)

@cl.delete('/delete-file')
def delete_file(delete: Delete):
    client.remove_object(delete.bucket_name,delete.object_name)
    

