from django.urls import path

from cinema.views import get_or_create_movie, get_update_or_delete_movie

app_name = "cinema"

urlpatterns = [
    path("cinema_movies/", get_or_create_movie, name="cinema_movies"),
    path("cinema_movies/<int:pk>", get_update_or_delete_movie, name="cinema_movie"),
]
