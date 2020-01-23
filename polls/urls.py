from django.urls import path

from . import views

urlpatterns = [
    path('', views.todays_date, name='date'),
]