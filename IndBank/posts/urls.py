from django.conf.urls import url
from .views import *
app_name = 'posts'
urlpatterns = [
    url(r'^signup$',add_user,name='add_user'),
    url(r'^logout$',user_logout,name='user_logout'),
    url(r'^home/(?P<username>[0-9A-Za-z\.@\-]+)$',homepage,name='homepage'),
    url(r'^profile/(?P<username>[0-9A-Za-z\.@\-]+)$',profile,name='profile'),    
    url(r'^login',user_login,name='user_login'),
    url(r'^$',login_page,name='login_page'),
    url(r'^submit$',add_post,name="submit_post")

]
