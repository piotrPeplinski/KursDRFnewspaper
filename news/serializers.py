from rest_framework import serializers, exceptions
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueValidator


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'owner', 'date')
        read_only_fields = ('id', 'date', 'owner')


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(
        many=True, queryset=Article.objects.all(), view_name='articleDetail')
    email = serializers.EmailField(
        required=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=[
                    'A user with that email already exists.']
            )
        ]
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'articles')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):  # request data
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')

        try:
            validate_password(password)
        except ValidationError as e:
            raise exceptions.ValidationError({'password': e.messages})
        else:
            if email:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
            else:
                user = User.objects.create_user(
                    username=username, password=password)
            return user
        
    def update(self, instance, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')

        try:
            validate_password(password)
        except ValidationError as e:
            raise exceptions.ValidationError({'password': e.messages})
        else:
            instance.username = username
            instance.set_password(password)
            if email:
                instance.email=email
            instance.save()
            return instance
