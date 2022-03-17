from pickle import TRUE
from rest_framework import serializers
from movies.models import Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")

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
