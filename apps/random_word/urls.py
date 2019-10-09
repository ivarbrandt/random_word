from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ran_word$', views.index),
    url(r'^ran_word/reset$', views.reset)
]