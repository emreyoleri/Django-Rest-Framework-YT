from django.urls import path, include
from news.api import views as api_views

urlpatterns = [
    path("articles/", api_views.ArticleListCreateAPIView.as_view(),
         name="article-list"),
    path("articles/<int:pk>", api_views.ArticleDetailAPIVIEW.as_view(),
         name="article-detail"),
]


# urlpatterns = [
#     path("articles/", api_views.article_list_create_api_view, name="article-list"),
#     path("articles/<int:pk>", api_views.article_detail_api_view,
#          name="article-detail"),
# ]
