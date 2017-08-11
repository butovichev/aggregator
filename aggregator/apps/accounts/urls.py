# from django.contrib.auth import logout, login
from django.conf.urls import url
from .views import signup

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
]
