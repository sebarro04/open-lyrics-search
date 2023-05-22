import os
from decouple import config
from azure.storage.blob import BlobServiceClient

class Blobstorage:
    def __init__(self):
        try:
            blobstorage_url = config('BLOBSTORAGE_URL')
            blobstorage_key = config('BLOBSTORAGE_KEY')
            self.blob_service_client = BlobServiceClient(blobstorage_url, credential=blobstorage_key)
            print('Blobstorage connected')
        except Exception as ex:
            print(f'Error connecting to the blob service client')
            raise

    def list_blobs_names(self, container_name: str) -> list[str] | None:
        try:
            container_client = self.blob_service_client.get_container_client(container=container_name)
            return [x for x in container_client.list_blob_names()]
        except Exception as ex:
            print(f'Error listing the blobs names: {ex}')
            return None
    
    def download_blob(self, container_name: str, file_url: str, download_path: str) -> None:
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=file_url)
            with open(os.path.join(download_path, file_url), mode='wb') as blob:
                download_stream = blob_client.download_blob()
                blob.write(download_stream.readall())
            print(f'{file_url} downloaded')
        except Exception as ex:
            print(f'Error downloading the blob: {ex}')
            return None
        
    def delete_local_blob(self, file_path: str) -> None:
        try:
            os.remove(file_path)
        except Exception as ex:
            print(f'Error deleting the temporary file: {ex}')
            return None

if __name__ == '__main__':
    blob_client = Blobstorage()