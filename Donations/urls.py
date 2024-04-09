from django.urls import path
from . import views

app_name = 'Donations'

urlpatterns = [
    path('new/', views.donates_form, name="new"),  # שולח לטופס
    path('Thankyou/', views.Thankyou, name="Thankyou"),  # שולח לטופס
    path('export_pdf', views.export_pdf, name="export_pdf"),
    path('export_excel', views.export_excel, name="export_excel"),


]
