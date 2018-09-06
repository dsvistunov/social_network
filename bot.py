#!/usr/bin/python

import string
import os
import sys
import random
from django.test import Client
from django.core.wsgi import get_wsgi_application
from django.utils.crypto import get_random_string
from dotenv import load_dotenv


if __name__ == "__main__":
	sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'api'))
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
	application = get_wsgi_application()

from api.v1.soc_net.models import Post


load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf.txt'))

client = Client()
number_of_users = int(os.getenv('number_of_users'))
max_posts_per_user = int(os.getenv('max_posts_per_user'))
max_likes_per_use = int(os.getenv('max_likes_per_use'))


def likes_post(token):
	posts = Post.objects.all()
	post = random.choice(posts) 
	client.post('/api/like/', data={
		"post": post.id
		},HTTP_AUTHORIZATION=token)


def create_post(token):
	title = get_random_string(32)
	body = get_random_string(250)
	client.post('/api/create/', data={
		"title": title,
		"body": body
		},HTTP_AUTHORIZATION=token)


def sign_up_user():
	username = get_random_string(8)
	email = username + '@mail.co'
	password = get_random_string(8)
	response = client.post('/rest-auth/registration/', data={
			"username": username,
			"email": email,
			"password1": password,
			"password2": password
		})
	try:
		token = response.json()['token']
		auth_token = 'JWT %s' % token
		number_posts = random.randint(1, max_posts_per_user)
		for _ in range(number_posts):
			create_post(auth_token)
		likes_post(auth_token)
	except KeyError:
		print(response.content)


def main():
	for _ in range(number_of_users):
		sign_up_user()

if __name__ == "__main__":
	main()