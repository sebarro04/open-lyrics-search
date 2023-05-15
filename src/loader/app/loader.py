import csv

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def load_artists_csv(filename: str) -> list | Exception:
    with open(filename, mode='r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
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
            print('Invalid csv format')
            return ex
    return artists_data

def load_lyrics_csv(filename: str) -> list:
    with open(filename, mode='r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
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
            print('Invalid csv format')
            return ex
    return lyrics_data

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

def load_data():
    songs = load_lyrics_csv('src/loader/tmp/lyrics-data.csv')
    #print(songs)
    artists = load_artists_csv('src/loader/tmp/artists-data.csv')
    #print(artists)
    linked_data = link_songs_with_artists(songs, artists)
    print(linked_data)

if __name__ == '__main__':
    load_data()