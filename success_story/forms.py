from django.forms import ModelForm
from .models import story


class storyForm(ModelForm):
    class Meta:
        model = story
        fields = ['date', 'name', 'text']
