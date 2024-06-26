from django.test import TestCase
from django.urls import reverse
from apps.users.models import User

class TestUsers(TestCase):
    def setUp(self):    
        self.user = User.objects.create_user(
            username="Akromjon",
            password="2007"
        )

    def test_login(self):
        response = self.client.login(username="Akromjon", password='2007')
        self.assertRedirects(response, 'gap/rooms')

    def testUrl(self):
        response1 = self.client.get(reverse('users:register'))
        response2 = self.client.get(reverse('users:login'))
        response3 = self.client.get(reverse('users:logout'))
        response4 = self.client.get(reverse('users:profile', kwargs={'id':self.user.id}))
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(response4.status_code, 302)