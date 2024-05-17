from rest_framework import viewsets

from posts.models import Comment, Group, Post
from .mixins import OnlyAuthorModificationMixin
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(OnlyAuthorModificationMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(OnlyAuthorModificationMixin):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs.get('post_id')
        )

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        return Comment.objects.filter(post=post)
