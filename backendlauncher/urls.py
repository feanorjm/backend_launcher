from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from admin_launcher.models import background
from rest_framework import routers
from admin_launcher.views import *
from admin_launcher.api import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'backgrounds', BackgroundViewSet)
router.register(r'apps', AppViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'trailers', TrailerViewSet)
router.register(r'descriptions', TrailerViewSet)
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), #Admin Django

    url(r'^api/', include(router.urls)), #Rest Framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), #Rest Framework

    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', gentella_html, name='gentella'),

    # The home page
    path('index/', index, name='index'),
    path('', index, name='index'),
    path('form_background/', background_create, name='background_create'),
]

