from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Article
from django.contrib.auth.models import User
from ..serializers import ArticleSerializer
from rest_framework import pagination
import random


class ReadArticlesTest(APITestCase):
    def setUp(self):
        self.urlList = reverse('articles')
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
        self.detailIndex = random.randint(0, len(self.articles)-1)
        self.urlRetrieve = reverse('articleDetail',args=[self.articles[self.detailIndex].id])
        self.expected_data = ArticleSerializer(self.articles, many=True)

    def test_list_articles(self):
        response = self.client.get(self.urlList)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_data.data)

    def test_retrieve_article(self):
        response = self.client.get(self.urlRetrieve) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_data.data[self.detailIndex])

class CreateArticleTest(APITestCase):
    def setUp(self):
        credentials = {'username':'testuser','password':'12345'}
        self.user = User.objects.create_user(**credentials)
        self.data = {'title':'Hello world', 'text':'Something interesting'}
        self.url = reverse('articles')
        self.client.force_authenticate(self.user)

    def test_create_article(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)