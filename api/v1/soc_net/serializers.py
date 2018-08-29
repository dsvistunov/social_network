from rest_framework.serializers import ModelSerializer
from api.v1.soc_net.models import Post, Like, Dislike


class PostCreateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'body']

	def create(self, validated_data):
		user = self.context['request'].user
		title = validated_data.pop('title')
		body = validated_data.pop('body')
		post = Post.objects.create(
			user=user,
			title=title,
			body=body
		)
		return post


class PostLikeCreateSerializer(ModelSerializer):
	class Meta:
		model = Like
		fields = ['post']

	def create(self, validated_data):
		user = self.context['request'].user
		post = validated_data.pop('post')
		like, created = Like.objects.get_or_create(
			user=user,
			post=post
		)
		if not created:
			like.delete()
		return like


class PostDislikeCreateSerializer(ModelSerializer):
	class Meta:
		model = Dislike
		fields = ['post']

	def create(self, validated_data):
		user = self.context['request'].user
		post = validated_data.pop('post')
		dislike, created = Dislike.objects.get_or_create(
			user=user,
			post=post
		)
		if not created:
			dislike.delete()
		return dislike
