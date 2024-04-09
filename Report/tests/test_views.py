from django.urls import reverse
from django.test import TestCase, Client
from Report.models import report


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = report.objects.create(name='report number 1',
                                         date='2024-04-24',
                                         text='help the family!')

    def test_all_reports_GET(self):
        ''' test if all reports page is displayed '''
        response = self.client.get(reverse('Report:all_reports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Report/all_reports.html')

    def test_create_report_GET(self):
        ''' test if the form is display '''
        response = self.client.get(reverse('Report:createReport'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Report/createReport.html')

    def test_create_report_POST_Valid(self):
        ''' test if function adds new report  '''
        report_count = report.objects.count()
        response = self.client.post(reverse('Report:createReport'), {'name': 'report number 1',
                                                                     'date': '2024-03-24',
                                                                     'text': 'help the family!'})

        self.assertEqual(response.status_code, 302)  # means redirection works
        self.assertEqual(report.objects.count(), report_count + 1)  # all fields are in place

    def test_create_report_POST_Not_Valid(self):
        ''' test the case of a bad form '''
        response = self.client.post(reverse('Report:createReport'),
                                    {'name': 'report number 1',
                                     'date': '24/03/2024',  # bad date form should not validate
                                     'text': 'help the family!'})
        self.assertEqual(response.status_code, 200)  # bad form we need to render a clean form

    def test_delete_report(self):
        ''' test the 'delete_report' function '''
        report_count = report.objects.count()  # counting prior to deletion
        response = self.client.get(reverse('Report:deleteReport', args=[self.obj.pk]))
        self.assertEqual(report.objects.count(), report_count - 1)  # comparing prior count to post deletion count
        self.assertEqual(response.status_code, 302)  # redirection code


