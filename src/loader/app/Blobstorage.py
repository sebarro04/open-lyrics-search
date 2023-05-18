import os
from decouple import config
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) # set absolute path to .py

class Blobstorage:
    def __init__(self):
        try:
            blobstorage_url =config('BLOBSTORAGE_URL')
            blobstorage_key = config('BLOBSTORAGE_KEY')
            self.blob_service_client = BlobServiceClient(blobstorage_url, credential=blobstorage_key)
            print('Connection to blobstorage successful')
        except Exception as ex:
            print('Error connecting to the blob service client')

    def list_blobs_names(self, container_name: str) -> list | None:
        try:
            container_client = self.blob_service_client.get_container_client(container=container_name)
            return [x for x in container_client.list_blob_names()]
        except Exception as ex:
            print('Error listing the blobs names')
            return None
    
    def download_blob(self, container_name: str, file_url: str) -> None:
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=file_url)
            with open(os.path.join(FILE_PATH, f'./temp-files/{file_url}'), mode='wb') as blob:
                download_stream = blob_client.download_blob()
                blob.write(download_stream.readall())
        except Exception as ex:
            print('Error downloading the blob')
            return None
        
    def delete_local_blob(self, filename: str) -> None:
        try:
            os.remove(os.path.join(FILE_PATH, f'./temp-files/{filename}'))
        except Exception as ex:
            print('Error deleting the temporary file')
            return None

if __name__ == '__main__':
    blob_client = Blobstorage()
    blob_client.download_blob('documents', 'artists-data-2.csv')