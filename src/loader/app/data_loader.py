import csv

def is_num(num: str) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False

def load_csv(file_path: str) -> tuple[int, list] | None:
    with open(file_path, mode='r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
        headers = csv_reader.fieldnames
        if 'Artist' in headers and 'Genres' in headers and 'Songs' in headers and 'Popularity' in headers and 'Link' in headers:
            artists_data = []
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
                if (is_num(row['popularity'])):
                    row['popularity'] = float(row['popularity'])
                row['genres'] = [x.strip() for x in row['genres'].split(';')] # split genres by ; and delete leading whitespaces
                artists_data.append(row)
            return 1, artists_data # 1 as flag to indicate artists
        elif 'ALink' in headers and 'SName' in headers and 'SLink' in headers and 'Lyric' in headers and 'language' in headers:
            lyrics_data = []
            for row in csv_reader:
                # key renaming
                row['artist_link'] = row.pop('ALink')
                row['song_name'] = row.pop('SName')
                row['song_link'] = row.pop('SLink')
                row['lyric'] = row.pop('Lyric')
                row['language'] = row.pop('language')
                lyrics_data.append(row)
            return 2, lyrics_data # 2 as flag to indicate lyrics
        raise Exception('Invalid csv format')

def link_lyrics_with_artists(lyrics: list, artists: list) -> list[dict]:
    linked_data = []
    for artist in artists:
        for lyric in lyrics:
            if artist['link'] == lyric['artist_link']:
                lyric['artist'] = artist
                linked_data.append(lyric)
    return linked_data

if __name__ == '__main__':
    print('data_loader')