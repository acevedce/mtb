from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.molecule_list, name='molecule_list'),
]