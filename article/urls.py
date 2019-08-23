from django.urls import path

from .views import ArticleView, ArticleDetails


urlpatterns = [
    path('', ArticleView.as_view()),
    path('<int:pk>', ArticleDetails.as_view())
]