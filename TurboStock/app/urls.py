from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('authenticate/', views.auth),
    path('login/', views.login),
    path('logout/', views.logout),
    path('store/new/', views.new_store, name='newStore'),
    path('store/create/', views.create_store, name='createStore'),
    path('store/<int:store_id>/', views.store, name='store'),
    path('store/<int:store_id>/delete/', views.delete_store, name='deleteStore'),
    path('store/<int:store_id>/aisle/<int:aisle_id>', views.aisle, name='aisle'),
    path('product/<int:product_id>/', views.product, name='product')
]
