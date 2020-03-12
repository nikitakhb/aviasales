from rest_framework import serializers


class WordListSerializer(serializers.ListSerializer):
    child = serializers.CharField()
