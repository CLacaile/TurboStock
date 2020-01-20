from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('authenticate/', views.auth),
    path('login/', views.login),
    path('logout/', views.logout),
    path('store/<int:store_id>/', views.store, name='store'),
]