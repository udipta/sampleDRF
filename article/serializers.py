'''
    Serializers allow complex data such as querysets and model instances
    to be converted to native Python datatypes that can then be easily
    rendered into JSON, XML or other content types.
'''

from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()

    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()

        return instance
