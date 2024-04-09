from django.forms import ModelForm
from .models import report


class ReportForm(ModelForm):
    class Meta:
        model = report
        fields = ['date', 'name', 'text']
