from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)


urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='articles'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='articleDetail'),
    # path('users/', views.ListCreateUser.as_view(), name='users'),
    path('update-user/<int:pk>/', views.UpdateUser.as_view(), name='update-user'),
    path('', views.APIRoot.as_view(), name='apiRoot'),
    path('auth/', include(router.urls)),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
