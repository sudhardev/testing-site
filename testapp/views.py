from django.shortcuts import render

from.models import *

import requests 

from testpy.tmdb_helpers import get_movies

from django.conf import settings



def movie_details(request):
    tmdb_api_key = '34d518706297f7ced3a25969c4a2e1c6'
    api_urls = f'https://api.themoviedb.org/3/movie/popular?api_key={tmdb_api_key}'
      
    

    movie_list = []
    base_image_url = 'https://image.tmdb.org/t/p/w200'  # Base URL for movie posters (adjust the 'w500' as per your requirements)

    
    response = requests.get(api_urls)
    movie_data = response.json()
    movies = movie_data['results']  # Assuming the movie list is under 'results' key

        
    for movie in movies:
            poster_path = movie['poster_path']
            backdrop_path = movie['backdrop_path']
            complete_poster_url = base_image_url + poster_path  # Complete URL for the movie poster
            complete_poster_url_2 = base_image_url + backdrop_path
            #print(f"Movie: {movie['title']}")
            #print(f"Poster URL: {complete_poster_url}")

            movie_details = {
                'title': movie['title'],
                'vote_average': movie['vote_average'],
                'release_date': movie['release_date'],
                'poster_path': complete_poster_url,
                'backdrop_path' : complete_poster_url_2,
                'overview' : movie['overview'],
            }
            movie_list.append(movie_details)

    context = {'movies': movie_list}

    #print(context)

    return render(request, 'testapp/test.html', context)


def movie(request,mid):


    tmdb_api_key = settings.TMDB_API_KEY
    api_urls = [
        f'https://api.themoviedb.org/3/movie/popular?api_key={tmdb_api_key}',
        # Add more API URLs here for additional movie details
    ]

    movie_list = []
    base_image_url = 'https://image.tmdb.org/t/p/w200'  # Base URL for movie posters (adjust the 'w500' as per your requirements)

    for api_url in api_urls:
        response = requests.get(api_url)
        movie_data = response.json()
        movies = movie_data['results']  # Assuming the movie list is under 'results' key

        title = None
        for movie in movies:
            poster_path = movie['poster_path']
            backdrop_path = movie['backdrop_path']
            complete_poster_url = base_image_url + poster_path  # Complete URL for the movie poster
            complete_poster_url_2 = base_image_url + backdrop_path
            #print(f"Movie: {movie['title']}")
            #print(f"Poster URL: {complete_poster_url}")

            if movie['title'] == mid:

                title = movie

                movie = title

            movie_details = {
                'title': movie['title'],
                'vote_average': movie['vote_average'],
                'release_date': movie['release_date'],
                'poster_path': complete_poster_url,
                'backdrop_path' : complete_poster_url_2,
                'overview' : movie['overview'],
            }
            movie_list.append(movie_details)

    context = {'movies': movie_list,'title':title}

    return render (request, 'testapp/seach.html',context)


def testapp(request):

    item = test.objects.all()

    context = {'item':item}

    return render(request,'testapp/test.html',context)
def mock(request,sub_id):

    ident = test.objects.get(pk=sub_id)

    context = {'ident':ident}

    return render (request,'testapp/mocktest.html',context)

#def search (request):


    #data = requests.get("https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc")
    
    if data :

        print(data)

    else: 
        None

       

    return render (request,'testapp/seach.html',context={'data':data})


# Create your views here.
