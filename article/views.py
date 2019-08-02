from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Article
from .serializers import ArticleSerializer

# Create your views here.


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})
