#!/usr/bin/python3

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def request_main_page(movie_id):
    result = requests.get(
        f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{movie_id}',
        headers={ 
            'X-API-KEY': 'bd5197a8-ad7e-4582-94b1-7d0a0e4f2ec3', 
            'Content-Type': 'application/json', 
        }
    ).json()

    remove_fields = [
        'posterUrl',
        'posterUrlPreview',
        'editorAnnotation',
        'isTicketsAvailable',
        'productionStatus',
        'hasImax',
        'has3D',
    ]

    for field in remove_fields:
        result.pop(field)

    result['countries'] = [elem['country'] for elem in result['countries']]
    result['genres'] = [elem['genre'] for elem in result['genres']]
    
    return result

print(request_main_page(301))

def _get_similars(movie_id):
    result = requests.get(
        f'https://kinopoiskapiunofficial.tech//api/v2.2/films/{movie_id}/similars',
        headers={ 
            'X-API-KEY': 'bd5197a8-ad7e-4582-94b1-7d0a0e4f2ec3', 
            'Content-Type': 'application/json', 
        }
    ).json()
    
    return [elem['filmId'] for elem in result['items']]


def _get_staff(movie_id):
    result = requests.get(
        f'https://kinopoiskapiunofficial.tech//api/v1/staff?filmId={movie_id}',
        headers={ 
            'X-API-KEY': 'bd5197a8-ad7e-4582-94b1-7d0a0e4f2ec3', 
            'Content-Type': 'application/json', 
        }
    ).json()

    staff_info = {
        'director': [],
        'actor': [],
        'producer': [],
    }

    for person in result:
        profession = person['professionKey'].lower()
        if profession in staff_info:
            record = {
                'personId': person['staffId'],
                'nameRu': person['nameRu'],
                'nameEn': person['nameEn'],
            }
            staff_info[profession].append(record)
    
    return staff_info


def parse_movie(movie_id):
    result = _request_main_page(movie_id)
    result['similars'] = _get_similars(movie_id)
    result.update(_get_staff(movie_id))
    return result


#.then(res => res.json())
#    .then(json => console.log(json))
#    .catch(err => console.log(err))