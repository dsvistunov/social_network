from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from api.v1.soc_net.models import Post, Like, Dislike
from .serializers import (
    PostCreateSerializer,
    PostLikeCreateSerializer,
    PostDislikeCreateSerializer,
)


class PostCreateAPIView(CreateAPIView):
    model = Post
    permission_classes = (IsAuthenticated,)
    serializer_class = PostCreateSerializer


class PostLikeCreateAPIView(CreateAPIView):
    model = Like
    permission_classes = (IsAuthenticated,)
    serializer_class = PostLikeCreateSerializer


class PostDislikeCreateAPIView(CreateAPIView):
    model = Dislike
    permission_classes = (IsAuthenticated,)
    serializer_class = PostDislikeCreateSerializer
