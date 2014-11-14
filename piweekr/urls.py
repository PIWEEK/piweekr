from django.conf.urls import patterns, include, url
from django.contrib import admin

from projects import urls as projects_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'piweekr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(projects_urls)),
)
