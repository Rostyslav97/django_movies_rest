from pickle import TRUE
from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")

class MovieDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    producers = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    class Meta:
        model = Movie
        exclude = ("draft",)