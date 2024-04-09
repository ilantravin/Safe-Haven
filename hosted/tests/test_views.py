from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from hosted.forms import CustomUserCreationForm

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.group_host = Group.objects.create(name='מארח')
        self.group_hosted = Group.objects.create(name='מתארח')

    def test_signup_view(self):
        response = self.client.get(reverse('hosted:signup'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'testuser2',
            'email': 'test2@test.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'category': 'hosted'
        }
        response = self.client.post(reverse('hosted:signup'), data)
        self.assertEqual(response.status_code, 302)  # 302 status code means redirection

    def test_login_view(self):
        response = self.client.get(reverse('hosted:login'))
        self.assertEqual(response.status_code, 200)

        data = {
            'username': 'testuser',
            'password': '12345'
        }
        response = self.client.post(reverse('hosted:login'), data)
        self.assertEqual(response.status_code, 302)  # 302 status code means redirection

    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('hosted:logout'))
        self.assertEqual(response.status_code, 302)  # 302 status code means redirection