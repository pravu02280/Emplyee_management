from django.contrib import admin
from django.conf.urls import  include,url
from .import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.hello_world),

]
