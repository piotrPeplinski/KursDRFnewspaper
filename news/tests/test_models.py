from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Article


class ArticleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.article = Article.objects.create(
            title='Test Article', text='This is a test article', owner=self.user)

    def test_article_title(self):
        article = Article.objects.get(id=self.article.id)
        self.assertEqual(article.title, 'Test Article')

    def test_article_text(self):
        article = Article.objects.get(id=self.article.id)
        self.assertEqual(article.text, 'This is a test article')

    def test_article_owner(self):
        article = Article.objects.get(id=self.article.id)
        self.assertEqual(article.owner, self.user)
