from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User

class PostTests(APITestCase):

    def test_view_post(self):
        
        url = reverse('blog_api')
