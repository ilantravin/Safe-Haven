import django_filters
from .models import hostReq


class host_filter(django_filters.FilterSet):
    class Meta:
        model = hostReq
        fields = ['city', 'rooms', 'beds', 'kosher', 'is_occupied']
