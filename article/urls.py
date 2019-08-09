from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


# ------------------------ ViewSet ---------------------------------------
from rest_framework.routers import DefaultRouter
from .apiviews import ArticleViewSet, UserViewSet, api_root
from rest_framework import renderers

article_list = ArticleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

article_detail = ArticleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

article_highlight = ArticleViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    # path('', api_root),
    path('articles/', article_list, name='article-list'),
    path('articles/<int:pk>/', article_detail, name='article-detail'),
    path('articles/<int:pk>/highlight/', article_highlight, name='article-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
]

router = DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('users', UserViewSet)


app_name = "articles"

# app_name will help us do a reverse look-up latter.

# ------------------------ GenericView ---------------------------------------
# from .views import ArticleDetails, ArticleList, UserDetail, UserList, api_root, ArticleHighlight

# urlpatterns = [
#
#     # path('', api_root),
#     path('articles/', ArticleList.as_view(), name='article-list'),
#     path('articles/<int:pk>', ArticleDetails.as_view(), name='article-detail'),
#
#     path('users/', UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
#
#
#     path('articles/<int:pk>/highlight/', ArticleHighlight.as_view()),
# ]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
