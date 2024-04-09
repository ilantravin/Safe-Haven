from django.shortcuts import render
from .models import AidOrg
from django.http import HttpResponse

# Create your views here.
def aid_org_list(request):
    aid_org  = AidOrg.objects.all().order_by('-date')
    return render(request, 'aid_org/aid_org_list.html',{'aid_org':aid_org})

def aid_org_detail(request, slug):

    aid_org = AidOrg.objects.get(slug=slug)
    return render(request, 'aid_org/aid_org_detail.html',{'aid_org':aid_org})