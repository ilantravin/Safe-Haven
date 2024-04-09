from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Donations.views import donates_form, Thankyou, export_pdf, export_excel


class TestUrls(SimpleTestCase):

    def test_donates_form_url_is_resolved(self):
        """Test if the URL is resolved to the correct view function."""
        url = reverse('Donations:new')
        self.assertEqual(resolve(url).func, donates_form)

    def test_Thankyou_url_is_resolved(self):
        """Test if the URL is resolved to the correct view function."""
        url = reverse('Donations:Thankyou')
        self.assertEqual(resolve(url).func, Thankyou)

    def test_export_pdf_url_is_resolved(self):
        """Test if the URL is resolved to the correct view function."""
        url = reverse('Donations:export_pdf')
        self.assertEqual(resolve(url).func, export_pdf)

    def test_export_excel_url_is_resolved(self):
        """Test if the URL is resolved to the correct view function."""
        url = reverse('Donations:export_excel')
        self.assertEqual(resolve(url).func, export_excel)
