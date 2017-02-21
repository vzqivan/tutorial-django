from django.conf.urls import include, url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'^$', views.post_list),
	url (r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='blog.views.post_detail')
]