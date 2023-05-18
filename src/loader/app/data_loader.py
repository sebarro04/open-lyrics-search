import csv
import Blobstorage

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def load_csv(filename: str) -> tuple[int, list] | Exception:
    with open(filename, mode='r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames
        print(headers)
        if 'Artist' in headers:
            artists_data = []
            try:
                for row in csv_reader:
                    # key renaming
                    row['name'] = row.pop('Artist')
                    row['genres'] = row.pop('Genres')
                    row['songs'] = row.pop('Songs')
                    row['popularity'] = row.pop('Popularity')
                    row['link'] = row.pop('Link')
                    # data transform
                    if (row['songs'].isnumeric()):
                        row['songs'] = int(row['songs'])  
                    if (isfloat(row['popularity'])):
                        row['popularity'] = float(row['popularity'])
                    row['genres'] = row['genres'].split(';')
                    artists_data.append(row)
            except Exception as ex:
                print(ex)
                return Exception('Invalid csv format')
            return 1, artists_data # 1 as flag to indicate artists
        lyrics_data = []
        try:
            for row in csv_reader:
                # key renaming
                row['artist_link'] = row.pop('ALink')
                row['song_name'] = row.pop('SName')
                row['song_link'] = row.pop('SLink')
                row['lyric'] = row.pop('Lyric')
                row['language'] = row.pop('language')
                lyrics_data.append(row)
        except Exception as ex:
            print(ex)
            return Exception('Invalid csv format')
        return 2, lyrics_data # 2 as flag to indicate lyrics

def link_songs_with_artists(songs: list, artists: list) -> list:
    linked_data = []
    for artist in artists:
        song_count = 0
        for song in songs:
            if artist['link'] == song['artist_link']:
                song['artist'] = artist
                linked_data.append(song)
                song_count += 1
        songs[song_count:]
    return linked_data

def load_data() -> None:
    blob_client = Blobstorage.Blobstorage()
    blob_names_list = blob_client.list_blobs_names('documents')
    print(blob_names_list)
    for blob_name in blob_names_list:
        print(f'Downloading {blob_name}')
        blob_client.download_blob('documents', blob_name)
        blob_client.delete_temporary_blob()

if __name__ == '__main__':
    load_data()
