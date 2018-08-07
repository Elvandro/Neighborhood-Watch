from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create_hood/$', views.create_hood, name='create_hood'),
    url(r'^join/(\d+)',views.join, name = 'join_hood'),
    url(r'^hood_home/$',views.hood_home,name = 'hood_home'),
    url(r'^exithood/(\d+)',views.exithood,name = 'exithood'),
    url(r'^create_business/$', views.create_business, name='create_business'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^create_comment/(?P<post_id>\d+)', views.create_comment, name='create_comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
