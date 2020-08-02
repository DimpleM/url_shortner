from django.conf.urls import include, url
from django.contrib import admin
from url_shortner import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name="home"),
    url(r'^shortner/$',views.shortner,name="short"),
    url(r'^retrieve/$',views.retrieve,name="retrieve"),
]