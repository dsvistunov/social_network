from django.conf.urls import url
from .views import (
    PostCreateAPIView,
    PostLikeCreateAPIView,
    PostDislikeCreateAPIView
)


urlpatterns = [
    url(r'^create/$', PostCreateAPIView.as_view(), name='post-create'),
    url(r'^like/$', PostLikeCreateAPIView.as_view(), name='post-like'),
    url(r'^dislike/$', PostDislikeCreateAPIView.as_view(), name='post-dislike'),
]
