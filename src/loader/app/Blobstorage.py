import os
from decouple import config
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

class Blobstorage:
    def __init__(self):
        try:
            blobstorage_url =config('BLOBSTORAGE_URL')
            blobstorage_key = config('BLOBSTORAGE_KEY')
            self.blob_service_client = BlobServiceClient(blobstorage_url, credential=blobstorage_key)
            print('Connection to blobstorage successful')
        except Exception as ex:
            print('Error connecting to the blob service client')

    def list_blobs_names(self, container_name: str) -> list:
        try:
            container_client = self.blob_service_client.get_container_client(container=container_name)
            return [x for x in container_client.list_blob_names()]
        except Exception as ex:
            print(ex)
            return Exception('Error listing the blobs names')
    
    def download_blob(self, container_name: str, file_url: str) -> None | Exception:
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=file_url)
            with open(file='src/loader/tmp/tmp.csv', mode='wb') as blob:
                download_stream = blob_client.download_blob()
                blob.write(download_stream.readall())
        except Exception as ex:
            print(ex)
            return Exception('Error downloading the blob')
        
    def delete_temporary_blob(self) -> None | Exception:
        try:
            os.remove('src/loader/tmp/tmp.csv')
        except Exception as ex:
            print(ex)
            return Exception('Error deleting the temporary file')

if __name__ == '__main__':
    blob_client = Blobstorage()
    print(blob_client.list_blobs_names('documents'))