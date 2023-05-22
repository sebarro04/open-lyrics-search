import os
import data_loader
import Blobstorage
import MongoDB

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) # set absolute path to .py

def main():
    print('Open Lyrics Search - Loader')
    blob_client = Blobstorage.Blobstorage()
    mongodb = MongoDB.MongoDB()
    print('-----')
    available_files = blob_client.list_blobs_names('documents')    
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
        print('-----')        
        blob_client.download_blob('documents', file, download_path)
        file_path = os.path.join(FILE_PATH, f'./temp-files/{file}')
        print(f'Processing {file}')
        result = data_loader.load_csv(file_path)
        if (result[0] == 1):
            artists += result[1]
        else:
            lyrics += result[1]
        blob_client.delete_local_blob(file_path)
        print(f'{file} processed')
    print('-----') 
    songs = []
    if artists == [] or lyrics == []:
        print('Artists or lyrics data missing')
        return
    print('Linking data')
    songs = data_loader.link_lyrics_with_artists(lyrics, artists)
    if songs == []:
        print('0 records were linked')
        return
    print('-----') 
    print('Uploading songs to Mongo Atlas')
    for song in songs:
        result = mongodb.create_song(song)
        if result == None:
            return
    print('-----')
    print('Uploading processed files to Mongo Atlas')
    for processed_file in files_to_process:
        temp = {'filename': processed_file}
        result = mongodb.create_processed_file(temp)
        if result == None:
            return
    del mongodb
    del blob_client
    print('-----') 
    print('All the files were processed')
    return

if __name__ == '__main__':
    main()