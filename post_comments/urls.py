from django.conf.urls import url

from .views import BlogView

urlpatterns = [
    url(r'^blog/(?P<blog_id>\d+)/$', BlogView.as_view(), name='blog_detail'),
    url(r'^blogs/$', BlogView.as_view(), name='blogs'),
]
