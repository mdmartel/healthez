from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.bootstrap_test,name='bootstrap_test'),
    path('db_test/', views.food_test,name='food_test'),
    path('db_test_add/<str:name>', views.food_add,name='food_add'),
    path('input/', views.search_test,name='search_test'),
    path('input/lookup', views.run_search,name='run_search'),
]