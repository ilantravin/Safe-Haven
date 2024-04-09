import unittest
from Donations.forms import Donations_Form



class TestForms(unittest.TestCase):
    def test_Add_Host_Form_valid_Data(self): 
        """ test form with valid data """
        form = Donations_Form(data={ 
            'name': 'avi',
            'id_number': '999999999',
            'amount': '999',
                })
        self.assertTrue(form.is_valid())  # form is valid so true expected

    def test_Add_Host_Form_no_Data(self):
        """ test form with no data """
        form = Donations_Form(data={})
        self.assertFalse(form.is_valid())  # form is not valid so false expected
        self.assertEqual(len(form.errors), 3)  # form has 3 required fields
