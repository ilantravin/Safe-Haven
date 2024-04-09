from django.forms import ModelForm
from django import forms
from .models import Donations


class Donations_Form(ModelForm):
    """ Donations form """
    class Meta:
        model = Donations
        fields = '__all__'