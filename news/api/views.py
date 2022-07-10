from distutils.log import error
from rest_framework import status  # for http request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from news.models import Article, Journalist
from news.api.serializers import ArticleSerializer, JournalistSerializer

# class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class JournalistCreateAPIView(APIView):

    def get(self, request):
        journalists = Journalist.objects.all()
        serializer = JournalistSerializer(journalists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleListCreateAPIView(APIView):

    def get(self, request):
        articles = Article.objects.filter(is_active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):

    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk=pk)
        return article_instance

    def get(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        article = self.get_object(pk=pk)
        article.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# ? FUNCTION METHOD
# @api_view(["GET", "POST"])
# def article_list_create_api_view(request, *args, **kwargs):

#     if request.method == "GET":
#         articles = Article.objects.filter(is_active=True)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def article_detail_api_view(request, pk):
#     try:

#         article_instance = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({
#             "errors": {
#                 "code": 404,
#                 "message": f"No value found for such an id:({pk})"
#             }
#         }, status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article_instance)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         article_instance.delete()
#         return Response({
#             "success": {
#                 "code": 204,
#                 "message": f"{(pk)} id numbered articles have been deleted"
#             }}, status=status.HTTP_204_NO_CONTENT)
