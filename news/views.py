from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User


@api_view(['GET', 'POST'])
def article_list(request, format=None):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        # return JsonResponse(serializer.data, safe=False)
        # if non-dict is returned you need to set safe=False
        return JsonResponse({'articles': serializer.data})
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.user = get_object_or_404(User, pk=1)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, articleId, format=None):
    # try:
    #     article = Article.objects.get(pk=articleId)
    # except Article.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    article = get_object_or_404(Article, pk=articleId)
    # get_object_or_404 is better bc above status code it also returns info: {"detail": "Not found."}
    if request.method == 'GET':
        serializer = ArticleSerializer(instance=article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
