from django.urls import reverse
from django.test import TestCase, Client
from aid_org.models import AidOrg

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.aid_org = AidOrg.objects.create(
            name='Test Aid Org',
            slug='test-aid-org',
            description='Test Description',
            website='www.test.com',
            date='2022-01-01T00:00Z',
            thumb='default.png'
        )
        # Use the correct URL pattern names based on your urls.py
        self.list_url = reverse('aid_org:list')
        self.detail_url = reverse('aid_org:detail', args=[self.aid_org.slug])

    def test_aid_org_list_view(self):   # Adjust the test name to match the view being tested
        """ Test if the list view returns the correct response."""
        response = self.client.get(self.list_url)   # Use the correct URL pattern name based on your urls.py
        self.assertEqual(response.status_code, 200) # Ensure the view returns a 200 status code
        self.assertTemplateUsed(response, 'aid_org/aid_org_list.html') # Ensure the correct template is used
        # Ensure the context contains the aid_orgs list, adjusted to your actual context variable if needed
        self.assertIn('aid_org', response.context)  
        self.assertTrue(response.context['aid_org'].exists())   # Ensure the context contains the aid_orgs list

    def test_aid_org_detail_view(self):     # Adjust the test name to match the view being tested
        """ Test if the detail view returns the correct response."""
        response = self.client.get(self.detail_url)     # Use the correct URL pattern name based on your urls.py
        self.assertEqual(response.status_code, 200)     
        self.assertTemplateUsed(response, 'aid_org/aid_org_detail.html')     
        self.assertEqual(response.context['aid_org'], self.aid_org)     # Ensure the correct aid_org object is passed to the context
