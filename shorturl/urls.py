from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="main mage"),
    path('counter/', views.get_url_call_counter),
    re_path(r'^(?P<short_url>\w{7})/', views.forvarding)
]
