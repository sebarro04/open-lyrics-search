import unittest
import pipelines

class TestPipelines(unittest.TestCase):
    def test_filter_generation(self):
        query = {'search': 'test', 'artist': ['Slipknot'], 'genre': ['Rock', 'Heavy Metal'], 'popularity': [1.0, 10.0], 'songs': [10, 100], 'language': ['es', 'en']}
        result = {
            'must': [
                {
                    'text': {
                        'path': { 'wildcard': '*' },
                        'query': 'test'
                    }
                }
            ],
            'filter': [
                {
                    'text': {
                        'path': 'artist.name',
                        'query': ['Slipknot']
                    },
                },
                {
                    'text': {
                        'path': 'artist.genres',
                        'query': ['Rock', 'Heavy Metal']
                    },
                },
                {
                    'range': {
                        'path': 'artist.popularity',
                        'gte': 1.0,
                        'lte': 10.0
                    },
                },
                {
                    'range': {
                        'path': 'artist.songs',
                        'gte': 10,
                        'lte': 100
                    },
                },
                {
                    'text': {
                        'path': 'language',
                        'query': ['es', 'en']
                    },
                }
            ]
        }
        self.assertEqual(pipelines.generate_pipeline_query(query), result, 'Wrong pipeline query')

    def test_generate_search_pipeline(self):
        query = {'search': 'test', 'artist': ['Slipknot'], 'genre': ['Rock', 'Heavy Metal'], 'popularity': [1.0, 10.0], 'songs': [10, 100], 'language': ['es', 'en']}
        result = [
            {
                '$search': {
                    'compound': {
                        'must': [
                            {
                                'text': {
                                    'path': { 'wildcard': '*' },
                                    'query': 'test'
                                }
                            }
                        ],
                        'filter': [
                            {
                                'text': {
                                    'path': 'artist.name',
                                    'query': ['Slipknot']
                                },
                            },
                            {
                                'text': {
                                    'path': 'artist.genres',
                                    'query': ['Rock', 'Heavy Metal']
                                },
                            },
                            {
                                'range': {
                                    'path': 'artist.popularity',
                                    'gte': 1.0,
                                    'lte': 10.0
                                },
                            },
                            {
                                'range': {
                                    'path': 'artist.songs',
                                    'gte': 10,
                                    'lte': 100
                                },
                            },
                            {
                                'text': {
                                    'path': 'language',
                                    'query': ['es', 'en']
                                },
                            }
                        ]
                    },
                    'highlight': {
                        'path': { 'wildcard': '*' }
                    }
                }
            },
            {
                '$project': {
                    '_id': 1,
                    'song_name': 1,
                    'lyric': 1,
                    "highlights": { "$meta": "searchHighlights" },
                    'score': { '$meta': 'searchScore' }
                }
            }
        ]
        self.assertEqual(pipelines.generate_search_pipeline(query), result, 'Wrong $search')

    def test_generate_search_meta_pipeline(self):
        query = {'search': 'test', 'artist': ['Slipknot'], 'genre': ['Rock', 'Heavy Metal'], 'popularity': [1.0, 10.0], 'songs': [10, 100], 'language': ['es', 'en']}
        result = [
            {
                '$searchMeta': {
                    'facet': {
                        'operator': {
                            'compound': {
                                'must': [
                                    {
                                        'text': {
                                            'path': { 'wildcard': '*' },
                                            'query': 'test'
                                        }
                                    }
                                ],
                                'filter': [
                                    {
                                        'text': {
                                            'path': 'artist.name',
                                            'query': ['Slipknot']
                                        },
                                    },
                                    {
                                        'text': {
                                            'path': 'artist.genres',
                                            'query': ['Rock', 'Heavy Metal']
                                        },
                                    },
                                    {
                                        'range': {
                                            'path': 'artist.popularity',
                                            'gte': 1.0,
                                            'lte': 10.0
                                        },
                                    },
                                    {
                                        'range': {
                                            'path': 'artist.songs',
                                            'gte': 10,
                                            'lte': 100
                                        },
                                    },
                                    {
                                        'text': {
                                            'path': 'language',
                                            'query': ['es', 'en']
                                        },
                                    }
                                ]
                            }
                        },
                        'facets': {
                            'artist_name': {
                                'type': 'string',
                                'path': 'artist.name'
                            },
                            'genres_facet': {
                                'type': 'string',
                                'path': 'artist.genres'
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
                                'path': 'language'
                            }
                        }
                    }
                }
            }                        
        ]
        self.assertEqual(pipelines.generate_search_meta_pipeline(query), result, 'Wrong $searchMeta')

unittest.main()
