from django.conf.urls import url
from . import views

urlpatterns = [
    url('',view.index, name='index' ),
]
