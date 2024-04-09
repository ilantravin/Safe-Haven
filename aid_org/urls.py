from django.urls import path
from. import views

app_name = 'aid_org'

urlpatterns = [
    path('', views.aid_org_list, name="list"),
    path('<slug:slug>/', views.aid_org_detail, name = "detail"),
]
