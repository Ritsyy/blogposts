from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^blog/(?P<blog_id>\d+)/$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^blogs/$', BlogListView.as_view(), name='blogs'),
]
