def generate_pipeline_query(query: dict) -> dict:
    must = []
    filter = []
    mapping = {'artist': 'artist.name', 'genre': 'artist.genres', 'popularity': 'artist.popularity', 'songs': 'artist.songs', 'language': 'language'} # query mapping to document paths
    for key in query:
        if key == 'search':
            if query[key][0] == '"' and query[key][len(query[key]) - 1] == '"':
                temp = {
                    'phrase': {
                        'path': { 'wildcard': '*' },
                        'query': query[key]
                    }
                }
                must.append(temp)
            else:
                temp = {
                    'text': {
                        'path': { 'wildcard': '*' },
                        'query': query[key]
                    }
                }
                must.append(temp)
        if key == 'artist' or key == 'genre' or key == 'language':
            temp = {
                'text': {
                    'path': mapping[key],
                    'query': query[key]
                }
            }
            filter.append(temp)
        elif key == 'popularity' or key == 'songs':
            temp = {
                'range': {
                    'path': mapping[key],
                    'gte': query[key][0],
                    'lte': query[key][1]
                }
            }
            filter.append(temp)
    compound = {'must': must, 'filter': filter}
    return compound

def generate_search_pipeline(query: dict) -> list:
    compound = generate_pipeline_query(query)
    pipeline = [
        {
            '$search': {
                'compound': compound,
                'highlight': {
                    'path': { 'wildcard': '*' },
                    'maxNumPassages': 1
                }
            }
        },
        {
            '$project': {
                '_id': 1,
                'song_name': 1,
                'highlights': { '$meta': 'searchHighlights' },
                'score': { '$meta': 'searchScore' }
            }
        },
        {
            '$limit': 1_000
        }
    ]
    return pipeline

def generate_search_meta_pipeline(query: dict) -> list:
    compound = generate_pipeline_query(query)
    pipeline = [
        {
            '$searchMeta': {
                'facet': {
                    'operator': {
                        'compound': compound
                    },
                    'facets': {
                        'artist_name': {
                            'type': 'string',
                            'path': 'artist.name',
                            'numBuckets': 25
                        },
                        'genres_facet': {
                            'type': 'string',
                            'path': 'artist.genres',
                            'numBuckets': 25
                        },
                        'popularity_facet': {
                            'type': 'number',
                            'path': 'artist.popularity',
                            'boundaries': [0, 50, 100, 150, 200],
                            'default': 'others'
                        },
                        'songs_facet': {
                            'type': 'number',
                            'path': 'artist.songs',
                            'boundaries': [0, 200, 400, 600, 800, 1000],
                            'default': 'others'
                        },
                        'language_facet': {
                            'type': 'string',
                            'path': 'language',
                            'numBuckets': 25
                        }
                    }
                }
            }
        }                       
    ]
    return pipeline