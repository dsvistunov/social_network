from django.conf.urls import url
from .views import PostCreateAPIView

urlpatterns = [
	url(r'^create/$', PostCreateAPIView.as_view(), name='post-create'),
]