from pydantic import BaseModel

class Upload(BaseModel):
    bucket_name: str
    object_name: str
    file_path: str

class Download(BaseModel):
    bucket_name: str
    object_name: str
    file_path: str

class Delete(BaseModel):
    bucket_name: str
    object_name: str