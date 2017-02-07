from django.conf.urls import url, include
from django.contrib import admin
from appfrequencia.views import home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^appfrequencia/', include('appfrequencia.urls')),
    url(r'^accounts/profile/$', home, name='home'),
    url(r'^$', home, name="home")
]
