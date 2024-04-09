from django.forms import ModelForm
from .models import hostReq


class HostForm(ModelForm):
    class Meta:
        model = hostReq
        fields = ['fullname', 'street', 'city' , 'housetype',
                  'rooms', 'beds', 'kosher','phone',
                  'email', 'description', 'thumb','is_occupied']
