from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('authenticate/', views.auth),
    path('login/', views.login),
    path('logout/', views.logout),
    path('<int:store_id>/', views.store, name='store'),
]