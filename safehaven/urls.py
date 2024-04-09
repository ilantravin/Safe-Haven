from django.contrib import admin
from django.urls import path, include
from. import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from safehaven import views
from django.shortcuts import redirect




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name='homepage'),
    path('hosted/',include('hosted.urls')),
    path('aid_org_list/', include('aid_org.urls')),
    path('about/',views.about, name='about'),
    path('success_story/', include('success_story.urls')),
    path('Donations/',include('Donations.urls'), name='Donations)'),
    path('Report/',include('Report.urls')),
    path('admin_page/', views.admin, name='admin_page'),
    path('reports',views.reports,name='reports'),
    path('forum/', include('forum.urls'), name='forum'),
    path('host/', include('host.urls'), name='host'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)