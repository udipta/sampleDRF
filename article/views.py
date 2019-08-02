from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Article

# Create your views here.


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        return Response({"articles": articles})
