from rest_framework import serializers

from .models import Post, Comment, User


class PostSerializers(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializers(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = '__all__'
        model = Comment


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
