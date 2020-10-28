from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^new/project$',views.new_project, name='new-project'),
    url(r'^site/(\d+)',views.site,name='site'),
   
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/countries/$', views.countriesList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)