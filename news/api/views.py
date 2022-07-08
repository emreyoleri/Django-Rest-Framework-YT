from rest_framework import status  # for http request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from news.models import Article
from news.api.serializers import ArticleSerializer


@api_view(["GET", "POST"])
def article_list_create_api_view(request, *args, **kwargs):

    if request.method == "GET":
        articles = Article.objects.filter(is_active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def article_detail_api_view(request, pk):
    try:

        article_instance = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({
            "errors": {
                "code": 404,
                "message": f"No value found for such an id:({pk})"
            }
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArticleSerializer(article_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        article_instance.delete()
        return Response({
            "success": {
                "code": 204,
                "message": f"{(pk)} id numbered articles have been deleted"
            }}, status=status.HTTP_204_NO_CONTENT)
