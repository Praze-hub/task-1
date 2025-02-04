from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    current_datetime = serializers.CharField()
    github_url = serializers.URLField()
