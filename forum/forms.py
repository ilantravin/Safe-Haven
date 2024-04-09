from django.forms import ModelForm
from .models import *


class CreateInForum(ModelForm):  # subject
    class Meta:
        model = forum
        fields = "__all__"


class CreateInDiscussion(ModelForm):  # comment
    class Meta:
        model = Discussion
        fields = ['name', 'forum', 'discuss']
