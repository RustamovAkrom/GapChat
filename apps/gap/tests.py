from django.test import TestCase
from django.urls import reverse

class TestGap(TestCase):
    def test_opinion(self):
        response = self.client.get(reverse("gap:room",kwargs={"pk":1}))

        
        print(response.context)