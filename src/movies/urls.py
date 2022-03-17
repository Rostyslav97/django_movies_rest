from django.urls import path
from movies.views import MovieListView, MovieDetailView

urlpatterns = [
    path("movies/", MovieListView.as_view()),
    path("movies/<int:pk>/", MovieDetailView.as_view())
]