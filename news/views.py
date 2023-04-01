from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly


class APIRoot(APIView):
    def get(self, request, format=None):
        links = {
            'users': reverse('users', request=request, format=format),
            'articles': reverse('articles', request=request, format=format),
            # add more links to other endpoints as needed
        }
        return Response(links)


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ListCreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        reqMethod = self.request.method
        return [permissions.IsAdminUser()] if reqMethod == 'GET' else [permissions.AllowAny()]
