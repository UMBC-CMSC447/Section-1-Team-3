from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from beach_homepage.views import search
from beach_homepage.views import sort
from beach_homepage.views import beach_propregister
from beach_homepage.views import beach_prop_info
from beach_homepage.views import beach_index
from beach_homepage.views import beach_redirect
from login.views import *
from upload.views import *
from regProperty.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^logout/$', logout_page),
    url(r'^upload/',ProfileImageView.as_view(), name = 'profile_image_upload'),
    url(r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(),
        name='profile_image'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^propregister/$', propregister),
    url(r'^propregister/success/$', propregister_success),
    url(r'^home/$', home),
    url(r'^search/prop_info/index.html',beach_index),
    url(r'^beach_homepage/prop_info/list_new_property.html',beach_redirect),
    url(r'^beach_homepage/prop_info/user_profile.html',beach_redirect),
    url(r'^beach_homepage/prop_info/list_new_property.html',beach_redirect),
    url(r'^search/prop_info/(.*)',beach_prop_info),
    url(r'^sort/(.*)',sort),
    url(r'^search/(.*)',search),
    url(r'^beach_homepage/list_new_property.html',beach_propregister),
    url(r'^beach_homepage/prop_info/index.html',beach_index),
    url(r'^beach_homepage/prop_info/(.*)',beach_prop_info),
    #it is important that this goes last like it is
    url(r'^beach_homepage/(.*)', include('beach_homepage.urls')),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
print(urlpatterns)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
