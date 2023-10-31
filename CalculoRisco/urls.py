from django.urls import path

from . import views

urlpatterns = [
    path('', views.calculo_risco, name='calculo_risco'),
]
