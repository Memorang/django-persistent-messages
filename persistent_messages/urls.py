from django.conf.urls import url

from persistent_messages import views


urlpatterns = [
    url(r'^detail/(?P<message_id>\d+)/$', views.message_detail, name='message_detail'),
    url(r'^mark_read/(?P<message_id>\d+)/$', views.message_mark_read, name='message_mark_read'),
    url(r'^mark_read/all/$', views.message_mark_all_read, name='message_mark_all_read'),
]
