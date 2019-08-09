"""
    Serializers allow complex data such as querysets and model instances
    to be converted to native Python datatypes that can then be easily
    rendered into JSON, XML or other content types.
"""
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    # new
    # highlight = serializers.HyperlinkedIdentityField(view_name='article-highlight', format='html')

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'code', 'author']
        # fields = ['url', 'id', 'highlight', 'title', 'description', 'code', 'author']


class UserSerializer(serializers.ModelSerializer):
# class UserSerializer(serializers.HyperlinkedModelSerializer):
    # new
    # articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail',
    #                                                queryset=Article.objects.all()
    #                                         )

    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'articles']
        # fields = ['url', 'id', 'username', 'articles']
