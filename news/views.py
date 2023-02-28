from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method=='GET':
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
