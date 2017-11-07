from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True), name= 'login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name= 'logout'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^song/$', views.songList, name = 'songList'),
    url(r'^song/(?P<id>[0-9]+)/$', views.individualSong, name = 'individualSong'),
    url(r'^letter/$', views.letter, name = 'letter'),
]
