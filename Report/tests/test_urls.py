import unittest
from django.urls import reverse, resolve
from Report.views import all_reports, createReport, deleteReport


class TestUrls(unittest.TestCase):
    def test_all_reports_url_is_resolved(self):
        url = reverse('Report:all_reports')
        self.assertEqual(resolve(url).func, all_reports)

    def test_createReport_url_is_resolved(self):
        url = reverse('Report:createReport')
        self.assertEqual(resolve(url).func, createReport)

    def test_deleteReport_url_is_resolved(self):
        url = reverse('Report:deleteReport', args=[1])
        self.assertEqual(resolve(url).func, deleteReport)
