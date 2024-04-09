from django.urls import path
from . import views

app_name = 'Report'

urlpatterns = [
    path('all_reports/', views.all_reports, name='all_reports'),
    path('createReport/', views.createReport, name='createReport'),
    path('deleteReport/<report_id>', views.deleteReport, name='deleteReport'),
]
