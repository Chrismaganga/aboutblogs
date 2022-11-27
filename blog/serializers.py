from blog.models import PublishedManager, Post, Comment
from rest_framework import serializers
# from django.contrib.auth.models import User
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = '__all__'


class PublishedManagerSerialiazer(serializers.SerializerMethodField):
    class Meta:
        model = PublishedManager




# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         read_only_fields = ["slug"]
#         fields = [
#             'author',
#             'title',
#             'slug',
#             'body',
#             'body',
#             'published',
#             'created',
#             'updated'
#         ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'post',
            'name',
            'email',
            'body',
            'created',
            'updated',
            'active'
        ]
        read_only_fields = [
            'slug'
            ]

