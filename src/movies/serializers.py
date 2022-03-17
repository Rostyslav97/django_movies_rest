from pickle import TRUE
from rest_framework import serializers
from movies.models import Movie, Rating, Review

class MovieSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")


class MovieListSerializer(serializers.ModelSerializer):
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ("id", "title", "tagline", "category", "rating_user", "middle_star")


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("name", "text", "parent")


class MovieDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    producers = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        exclude = ("draft",)


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("star", "movie")

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
        ip=validated_data.get('ip', None),
        movie=validated_data.get('movie', None),
        defaults={'star': validated_data.get("star")}
        )
        return rating