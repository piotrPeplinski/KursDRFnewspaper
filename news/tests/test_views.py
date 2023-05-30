from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Article
from django.contrib.auth.models import User
from ..serializers import ArticleSerializer
from rest_framework import pagination


class ArticleListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('articles')
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.articles = [
            Article.objects.create(
                title='Test Article 1', text='This is a test article', owner=self.user),
            Article.objects.create(
                title='Test Article 2', text='This is a test article', owner=self.user),
            Article.objects.create(
                title='Test Article 3', text='This is a test article', owner=self.user)
        ]
        pagination.PageNumberPagination
        self.expected_data = ArticleSerializer(self.articles, many=True)

    def test_list_articles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, self.expected_data.data)
