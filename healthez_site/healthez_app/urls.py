from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.bootstrap_test,name='bootstrap_test')
]