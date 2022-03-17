from django.urls import path
from movies.views import MovieListView, MovieDetailView, ReviewCreateView, AddStarRatingView

urlpatterns = [
    path("movies/", MovieListView.as_view()),
    path("movies/<int:pk>/", MovieDetailView.as_view()),
    path("review/", ReviewCreateView.as_view()),
    path("rating/", AddStarRatingView.as_view()),
]