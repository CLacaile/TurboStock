from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:store_id>/', views.store, name='store'),
]