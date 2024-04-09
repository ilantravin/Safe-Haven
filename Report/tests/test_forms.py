import unittest
from Report.forms import ReportForm


class TestForms(unittest.TestCase):
    def test_Report_Form_valid_Data(self):
        form = ReportForm(data=
                         {'name': 'report number 1',
                          'date': '2023-12-12',
                          'text': 'help!'})
        self.assertTrue(form.is_valid())  # form is valid so true expected

    def test_Report_Form_no_Data(self):
        form = ReportForm(data={})
        self.assertFalse(form.is_valid())  # form is not valid, so false expected
        self.assertEqual(len(form.errors), 2)
