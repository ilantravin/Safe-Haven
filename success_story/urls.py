from django.urls import path
from . import views

app_name = 'success_story'

urlpatterns = [
    path('all_stories/', views.all_stories, name='all_stories'),
    path('create_story/', views.create_story, name='create_story'),
]