from django.shortcuts import render
from rest_framework import generics
from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

post_list_create_view = PostListCreateAPIView.as_view()


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)


post_update_view = PostUpdateAPIView.as_view()


class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


post_destroy_view = PostDestroyAPIView.as_view()


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_content_negotiation(self, request, force=False):
        return super().perform_content_negotiation(request, force)


post_detail_view = PostDetailAPIView.as_view()



class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

commment_list_create_view = CommentListCreateAPIView.as_view()


class CommentUpdateAPIView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)


comment_update_view = CommentUpdateAPIView.as_view()


class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


comment_destroy_view = CommentDestroyAPIView.as_view()


class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_content_negotiation(self, request, force=False):
        return super().perform_content_negotiation(request, force)


comment_detail_view = PostDetailAPIView.as_view()



