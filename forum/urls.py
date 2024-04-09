from django.urls import path, re_path

from .views import addInForum, addInDiscussion, home

app_name = 'forum'

urlpatterns = [
    path('home/', home, name='home'),
    path('addInForum/', addInForum, name='addInForum'),
    path('addInDiscussion/', addInDiscussion, name='addInDiscussion'),

]
