from django.contrib import admin
from django.urls import path,include
from jilla.views import log,home,data,reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",reg),
    path("login",data),
    path("done",log),
    path("shop",home)
]
