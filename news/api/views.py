from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from news.models import Article
from news.api.serializers import ArticleSerializer


@api_view(["GET"])
def article_list_create_api_view(request):

    if request.method == "GET":
        articles = Article.objects.filter(is_active=True)
        serializer = ArticleSerializer(articles)  # error
        return Response(serializer.data)
