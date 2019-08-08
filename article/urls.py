from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleDetails, ArticleList, UserDetail, UserList

'''
from rest_framework.routers import DefaultRouter
from .apiviews import ArticleViewset

router = DefaultRouter()
router.register('Article', ArticleViewset, base_name='Article')
'''
app_name = "articles"

# app_name will help us do a reverse look-up latter.

urlpatterns = [

    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>', ArticleDetails.as_view(), name='article-detail'),

    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]

# urlpatterns += router.urls
urlpatterns = format_suffix_patterns(urlpatterns)