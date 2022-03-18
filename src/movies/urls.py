from django.urls import path
from movies.views import ActorsDetailView, MovieListView, MovieDetailView, ReviewCreateView, AddStarRatingView, ActorsListView, ActorDetailSerializer

urlpatterns = [
    path("movies/", MovieListView.as_view()),
    path("movies/<int:pk>/", MovieDetailView.as_view()),
    path("review/", ReviewCreateView.as_view()),
    path("rating/", AddStarRatingView.as_view()),
    path("actors/", ActorsListView.as_view()),
    path("actors/<int:pk>/", ActorsDetailView.as_view()),
]