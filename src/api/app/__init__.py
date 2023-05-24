import pymongo
import dns

from pymongo import MongoClient
from bson import ObjectId


client = pymongo.MongoClient("mongodb+srv://geraldnc88:GNCia2002#@cluster0.ibhh1cq.mongodb.net/")
""" result = client['open_lyrics_search']['songs'].aggregate([
    {
        '$search': {
            'index': 'default',
            'text': {
                'query': "Fim de baile, fim de noite",
                'path': 'lyric'
            }
        }
    }, {
        '$limit': 5
    },
    {
        '$project': {
            '_id': 1,
            'song_name': 1,
            'lyric': 1
        }
    }
]) """
result = client['open_lyrics_search']['songs'].aggregate([
    {
        '$match': {
            '_id': ObjectId("646c1870246a303032cea3c5")
        }
    },
    {
        '$project': {
            '_id': 1,
            'song_name': 1,
            'lyric': 1
        }
    }
])


for i in result:

    print(i)
    print("\n"+"\n")


