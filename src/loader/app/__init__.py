import data_loader
import Blobstorage
import MongoDB

if __name__ == '__main__':
    print('Hello Docker')
    blob_client = Blobstorage.Blobstorage()
    blob_client.download_blob('documents', 'artists-data-2.csv')
