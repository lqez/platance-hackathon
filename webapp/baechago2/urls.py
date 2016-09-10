from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from cav import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fetch/$', views.fetch, name='fetch'),
    url(r'^simulate/$', views.simulate, name='simulate'),
    url(r'^admin/', admin.site.urls),
] + staticfiles_urlpatterns()
