from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles')
    # adding related_name is neccessary for reverse relationship to work in serializer (PrimaryKeyRelatedField)
    
    def __str__(self):
        return f'{self.title} | {self.owner}'
