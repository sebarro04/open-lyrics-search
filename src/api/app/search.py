from MongoDB import MongoDB
from bson import ObjectId

def search_song__by_id(song_id) -> int | Exception:
    try:
        db = MongoDB()
        songs_collection = db.client['open_lyrics_search']['songs']  
        query = [{ '$match': { '_id': ObjectId(song_id) } }] 
        result = songs_collection.aggregate(query)
        song = next(result, None) 
        return song 
    except Exception as ex:
        print(ex)
        return ex
    

if __name__ == '__main__':
    print(search_song__by_id('646c1870246a303032cea3c5'))