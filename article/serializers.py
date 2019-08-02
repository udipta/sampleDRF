'''
    Serializers allow complex data such as querysets and model instances
    to be converted to native Python datatypes that can then be easily
    rendered into JSON, XML or other content types.
'''

from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
