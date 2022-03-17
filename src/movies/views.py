from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieDetailSerializer

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class MovieDetailView(APIView):
    def get(self, request, pk):
        movies = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movies)
        return Response(serializer.data)