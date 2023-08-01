import requests

def get_movies(api_key):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}" or f"https://api.themoviedb.org/3/movie/movie_id?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['results']
