from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly
from .paginators import ArticlePaginator
from rest_framework import filters, viewsets


class APIRoot(APIView):
    def get(self, request, format=None):
        links = {
            'users': reverse('user-list', request=request, format=format),
            'articles': reverse('articles', request=request, format=format),
            # add more links to other endpoints as needed
        }
        return Response(links)


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # pagination_class = ArticlePaginator
    # filter_backends = [filters.OrderingFilter]
    # ordering = ['-date']

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


class UpdateUser(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
