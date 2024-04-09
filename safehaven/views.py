from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def homepage(request):
    
    return render(request, 'homepage.html')


def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')

def admin(request):
    return redirect('/admin/')

def reports(request):
    return render(request, 'reports.html')

