from django.urls import path
from django.conf.urls import url
from . import views

app_name='shorturl'
urlpatterns = [
    path('', views.index, name="main mage"),
    path('counter/', views.ger_url_call_counter),
    url(r'^\w{7}/', views.forvarding)

]
