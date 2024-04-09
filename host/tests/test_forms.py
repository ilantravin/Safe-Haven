from django.test import TestCase
from host.forms import HostForm
from host.models import hostReq

class HostFormTest(TestCase):

    def test_form_validity(self):
        """Test if the HostForm is valid with given data"""
        data = {
            'fullname': 'Test Name',
            'street': 'Test Street',
            'city': 'Test City',
            'housetype': 'Test House Type',
            'rooms': 3,
            'beds': 2,
            'kosher': True,
            'phone': '1234567890',
            'email': 'test@test.com',
            'description': 'Test Description',
            'thumb': 'test.jpg',
            'is_occupied': False
        }
        form = HostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalidity(self):
        """Test if the HostForm is invalid with missing data"""
        form = HostForm(data={})
        self.assertFalse(form.is_valid())