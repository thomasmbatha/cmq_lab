from django.urls import path
from . import views

urlpatterns = [
    path('', views.egg_quality, name='egg'),
]