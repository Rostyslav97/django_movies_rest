from django.db import models
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from movies.models import Movie, Actor
from movies.serializers import CreateRatingSerializer, MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer, ActorListSerializer, ActorDetailSerializer
from movies.services import get_client_ip


class MovieListView(ListAPIView):
    serializer_class = MovieListSerializer
    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user = models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return movies


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieDetailSerializer


class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewCreateSerializer


class AddStarRatingView(CreateAPIView):
    serializer_class = CreateRatingSerializer
    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class ActorsListView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorsDetailView(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer


# class MovieListView(APIView):
#     def get(self, request):
#         movies = Movie.objects.filter(draft=False).annotate(
#             rating_user = models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(request)))
#         ).annotate(
#             middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
#         )
#         serializer = MovieListSerializer(movies, many=True)
#         return Response(serializer.data)


# class MovieDetailView(APIView):
#     def get(self, request, pk):
#         movies = Movie.objects.get(id=pk, draft=False)
#         serializer = MovieDetailSerializer(movies)
#         return Response(serializer.data)


# class ReviewCreateView(APIView):
#     def post(self, request):
#         review = ReviewCreateSerializer(data=request.data)
#         if review.is_valid():
#             review.save()
#         return Response(status=201)


# class AddStarRatingView(APIView):
#     def post(self, request):
#         serializer = CreateRatingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(ip=get_client_ip(request))
#             return Response(status=201)
#         else:
#             return Response(status=400)  