from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer

import coreapi
from rest_framework.schemas import AutoSchema


class ArticleViewSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('title'),
                coreapi.Field('description'),
            ]
            manual_fields = super().get_manual_fields(path, method)
            return manual_fields + extra_fields

# Create your views here.


class ArticleView(APIView):

    schema = ArticleViewSchema()

    def get(self, request):
        articles = Article.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        # serializer.author = request.user
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    schema = ArticleViewSchema()

    def get(self, request, pk):
        # articles = Article.objects.get(pk=self.kwargs.get('pk'))
        articles = Article.objects.filter(pk=pk).all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        article = Article.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
