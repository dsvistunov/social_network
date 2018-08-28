from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from api.v1.soc_net.models import Post
from .serializers import PostCreateSerializer


class PostCreateAPIView(CreateAPIView):
	model = Post
	permission_classes = (IsAuthenticated,)
	serializer_class = PostCreateSerializer
