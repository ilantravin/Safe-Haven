from django.test import TestCase
from django.contrib.auth.models import User
from hosted.forms import CustomUserCreationForm

class CustomUserCreationFormTest(TestCase):

    def test_form_validity(self):
        """Test if the CustomUserCreationForm is valid with given data"""
        data = {
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'category': 'hosted'
        }
        form = CustomUserCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalidity(self):
        """Test if the CustomUserCreationForm is invalid with missing data"""
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())