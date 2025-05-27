import requests

API_KEY = 'your_api_key_here'  # Replace this with your OMDb API key
BASE_URL = 'http://www.omdbapi.com/'

def search_movies(query):
    response = requests.get(BASE_URL, params={'apikey': API_KEY, 's': query})
    return response.json()

def get_movie_details(imdb_id):
    response = requests.get(BASE_URL, params={'apikey': API_KEY, 'i': imdb_id})
    return response.json()
