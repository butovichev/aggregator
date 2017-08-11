from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('aggregator.apps.accounts.urls')),
    url(r'^articles/', include('aggregator.apps.articles.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]


