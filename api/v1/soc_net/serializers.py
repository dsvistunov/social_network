from rest_framework.serializers import ModelSerializer
from api.v1.soc_net.models import Post


class PostCreateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'body']

	def create(self, validated_data):
		print(self.context['request'].user)
		user = self.context['request'].user
		title = validated_data.pop('title')
		body = validated_data.pop('body')
		post = Post.objects.create(
			user=user,
			title=title,
			body=body
		)
		return post
