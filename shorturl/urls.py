from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.main_page, name="main mage"),
    url(r'^\w{7}/', views.forvarding)
]
