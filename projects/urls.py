from django.conf.urls import *

from projects.routers import router

urlpatterns = patterns('',
    url(r'', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
