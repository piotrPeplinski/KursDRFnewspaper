from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='articles'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='articleDetail'),
    path('users/', views.ListCreateUser.as_view(), name='users'),
    path('update-user/<int:pk>/', views.UpdateUser.as_view(), name='update-user'),
    path('', views.APIRoot.as_view(), name='apiRoot'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
