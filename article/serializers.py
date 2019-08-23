'''
    Serializers allow complex data such as querysets and model instances
    to be converted to native Python datatypes that can then be easily
    rendered into JSON, XML or other content types.
'''

from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        # fields = ['id', 'title', 'description', 'author']
        fields = '__all__'
