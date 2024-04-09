from django.test import TestCase, Client
from django.urls import reverse
from Donations.models import Donations


class TestViews(TestCase):
    def setUp(self):
        """ setup for tests"""
        self.client = Client()
        self.obj = Donations.objects.create(id=1,
                                            name='Rex',
                                            id_number='999999999',
                                            amount='200',
                                            credit_number='9999999999999999',
                                            cvc='123'
                                            )
    def test_donates_form_GET(self):
        """ test form with valid data"""
        response = self.client.get(reverse('Donations:new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_layout.html')
        self.assertTemplateUsed(response, 'Donations/index.html')

    def test_donates_form_POST_Valid(self):
        """ test form with valid data"""
        Donations_count = Donations.objects.count()
        response = self.client.post(reverse('Donations:new'), {'name':'Rex',
                                            'id_number':'999999999',
                                            'amount':'200',
                                            'credit_number':'9999999999999999',
                                            'cvc':'123'})

        self.assertEqual(response.status_code, 302)  # means redirection works
        self.assertEqual(Donations.objects.count(), Donations_count+1)  # all fields are in place

