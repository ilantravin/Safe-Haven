from django.test import SimpleTestCase
from django.urls import reverse, resolve
from host import views

class TestUrls(SimpleTestCase):

    def test_all_hosts_url(self):
        url = reverse('host:all_hosts')
        self.assertEqual(resolve(url).func, views.all_hosts)

    def test_create_host_url(self):
        url = reverse('host:create_host')
        self.assertEqual(resolve(url).func, views.create_host)

    def test_delete_host_url(self):
        url = reverse('host:delete_host', args=['some-host-id'])
        self.assertEqual(resolve(url).func, views.delete_host)

    def test_edit_host_url(self):
        url = reverse('host:edit_host', args=[1])
        self.assertEqual(resolve(url).func, views.edit_host)

    def test_export_pdf_url(self):
        url = reverse('host:export_pdf')
        self.assertEqual(resolve(url).func, views.export_pdf)

    def test_export_excel_url(self):
        url = reverse('host:export_excel')
        self.assertEqual(resolve(url).func, views.export_excel)