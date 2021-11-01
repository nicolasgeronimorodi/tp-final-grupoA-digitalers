from django.urls import path

from . import views

urlpatterns = [
    path('', views.Api.as_view(), name='index'),
    path('<str:pk>', views.redir, name='redir'),#para redireccionar
]