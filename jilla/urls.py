from django.urls import path
from . import views

urlpatterns=[
  path('',views.reg, name="register"),
  path('login',views.data, name="log"),
  path('done',views.log, name="done"),
  path('shop',views.home, name="home")
]