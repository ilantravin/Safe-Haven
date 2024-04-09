from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hosted import views

class TestUrls(SimpleTestCase):

    def test_signup_url(self):
        url = reverse('hosted:signup')
        self.assertEqual(resolve(url).func, views.signup_view)

    def test_login_url(self):
        url = reverse('hosted:login')
        self.assertEqual(resolve(url).func, views.login_view)

    def test_logout_url(self):
        url = reverse('hosted:logout')
        self.assertEqual(resolve(url).func, views.logout_view)