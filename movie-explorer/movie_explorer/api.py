import requests

API_KEY = '82cca542'  # Replace with your real key
BASE_URL = 'http://www.omdbapi.com/'

def search_movies(query):
    response = requests.get(BASE_URL, params={'apikey': API_KEY, 's': query})
    data = response.json()
    # Debug output
    print(f"DEBUG: Request URL: {response.url}")
    print(f"DEBUG: Response JSON: {data}")
    return data

def get_movie_details(imdb_id):
    response = requests.get(BASE_URL, params={'apikey': API_KEY, 'i': imdb_id})
    data = response.json()
    # Debug output
    print(f"DEBUG: Request URL: {response.url}")
    print(f"DEBUG: Response JSON: {data}")
    if data.get('Response') == 'True':
        return data
    else:
        return None
