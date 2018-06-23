from django.conf.urls import url
from posts.views import post_create,post_delete,post_update,post_list,post_detail
app_name='posts'
urlpatterns = [
    url('create/',post_create,name='post_detail'),
    url('(?P<id>\d+)/edit',post_update,name='post_update'),
    url('list',post_list,name='post_list'),
    url(r'^(?P<id>\d+)/$',post_detail,name='post_detail'),
    url(r'^(?P<id>\d+)/delete$',post_delete,name='post_delete')  #appname.views.viewname
]

