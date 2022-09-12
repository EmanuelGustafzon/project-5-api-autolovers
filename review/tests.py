from django.contrib.auth.models import User
from .models import Review
from rest_framework import status
from rest_framework.test import APITestCase


class ReviewListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='Emanuel', password='pass')

    def test_can_list_reviews(self):
        Emanuel = User.objects.get(username='Emanuel')
        Review.objects.create(owner=Emanuel, model_year=1998)
        response = self.client.get('/review/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

 
