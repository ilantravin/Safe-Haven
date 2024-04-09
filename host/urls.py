from django.urls import path
from . import views

app_name = 'host'

urlpatterns = [
    path('all_hosts/', views.all_hosts, name='all_hosts'),
    path('create_host/', views.create_host, name='create_host'),
    path('delete_host/<host_id>', views.delete_host, name='delete_host'),
    path('edit_host/<int:host_id>/', views.edit_host, name='edit_host'),
    path('export_pdf', views.export_pdf, name="export_pdf"),
    path('export_excel', views.export_excel, name="export_excel"),
]