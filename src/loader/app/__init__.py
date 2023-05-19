import os
import data_loader
import Blobstorage
import MongoDB

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) # set absolute path to .py

def main():
    print('Open Lyrics Search - Loader')
    blob_client = Blobstorage.Blobstorage()
    mongodb = MongoDB.MongoDB()
    available_files = blob_client.list_blobs_names()    
    processed_files = mongodb.read_processed_files()
    files_to_process = []
    for file in available_files:
        if (file not in processed_files):
            files_to_process.append(file)
    if files_to_process == []:
        print('There are no files to process')
        return
    print(f'{len(files_to_process)} files to process')
    artists = []
    lyrics = []    
    download_path = os.path.join(FILE_PATH, './temp-files')
    for file in files_to_process:
        print(f'Processing {file}')
        blob_client.download_blob('documents', file, download_path)
        file_path = os.path.join(FILE_PATH, f'./temp-files/{file}')
        result = data_loader.load_csv(file_path)
        if (result[0] == 1):
            artists.append(result[1])
        else:
            lyrics.append(result[1])
        blob_client.delete_local_blob(file_path)
    linked_data = []
    if artists == [] or lyrics == []:
        print('Artists or lyrics data missing')
        return
    linked_data = data_loader.link_lyrics_with_artists(lyrics, artists)
    if linked_data == []:
        print('0 records were linked')
        return
    result = mongodb.create_songs(linked_data)
    if isinstance(result, None):
        return
    mongodb.create_processed_files(files_to_process)
    return

if __name__ == '__main__':
    main()