from rest_framework import serializers
from news.models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    text = serializers.CharField()
    city = serializers.CharField()
    release_date = serializers.DateField()
    is_active = serializers.BooleanField()
    creation_date = serializers.DateTimeField(read_only=True)
    date_of_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description)
        instance.text = validated_data.get("text", instance.text)
        instance.city = validated_data.get("city", instance.city)
        instance.is_active = validated_data.get(
            "is_active", instance.is_active)
        instance.release_date = validated_data.get(
            "release_date", instance.release_date)
        instance.creation_date = validated_data.get(
            "creation_date", instance.creation_date)
        instance.date_of_update = validated_data.get(
            "date_of_update", instance.date_of_update)

        instance.save()

        return instance

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError(
                "Title and description fields cannot be the same. please enter a different value")
        return data

    def validate_title(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                f"The title field must be at least 20 characters. you entered ({len(value)}) characters")
        return value
