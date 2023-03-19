from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
