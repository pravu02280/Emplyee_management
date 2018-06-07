from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^courses/', include('courses.urls')),
        url('admin/', admin.site.urls),
        url(r'^$', views.hello_world),

]
