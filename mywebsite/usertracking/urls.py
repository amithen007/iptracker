# usertracking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.track_visitor, name='track_visitor'),
    path('visitors/', views.visitor_list, name='visitor_list'),
]
