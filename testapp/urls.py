from django.contrib import admin
from django.urls import path,include
from.import views

app_name = "testapp"

urlpatterns = [
    path('',views.movie_details,name='movies-list'),
    path('<int:sub_id>/',views.mock,name='mocktest'),
    path('movies/<str:mid>/',views.movie,name='movie'),
]
