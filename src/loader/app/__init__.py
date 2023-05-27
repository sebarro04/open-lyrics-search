import os
import data_loader
import Blobstorage
import MongoDB
import speedtest

CURRENT_FILE_PATH = os.path.dirname(os.path.abspath(__file__)) # set absolute path to .py

def main():
    st = speedtest.Speedtest()    
    print('Open Lyrics Search - Loader')
    print('-----')
    print(f'Download speed Mbps: {round(st.download() / 1000 / 1000, 1)}')
    print(f'Upload speed Mbps: {round(st.upload() / 1000 / 1000, 1)}')
    print('-----')
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
    download_path = os.path.join(CURRENT_FILE_PATH, './temp-files')
    for file in files_to_process:
        print('-----')        
        blob_client.download_blob('documents', file, download_path)
        file_path = os.path.join(CURRENT_FILE_PATH, f'./temp-files/{file}')
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
    print(f'Uploading {len(songs)} songs to Mongo Atlas')
    while songs != []:
        result = mongodb.create_songs(songs[:1000])
        if result == None:
            return
        songs = songs[1000:]     
    processed_files = []
    for file in files_to_process:
        processed_files.append({'filename': file})
    print('-----')
    print(f'Uploading {len(processed_files)} processed files to Mongo Atlas')
    while processed_files != []:
        result = mongodb.create_processed_files(processed_files[:1000])
        if result == None:
            return
        processed_files = processed_files[1000:]
    del mongodb
    del blob_client
    print('-----') 
    print('All the files were processed')
    return

if __name__ == '__main__':
    main()