from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name ='home'),

    path('authenticate/', views.auth),
    path('login/', views.login),
    path('logout/', views.logout),

    path('store/new/', views.new_store, name='newStore'),
    path('store/create/', views.create_store, name='createStore'),
    path('store/<int:store_id>/', views.store, name='store'),
    path('store/<int:store_id>/delete/', views.delete_store, name='deleteStore'),
    path('store/<int:store_id>/update/', views.delete_store, name='updateStore'),

    path('store/<int:store_id>/aisle/<int:aisle_id>', views.aisle, name='aisle'),
    path('store/<int:store_id>/aisle/create/', views.create_aisle, name='createAisle'),
    path('store/<int:store_id>/aisle/new/', views.new_aisle, name='newAisle'),
    path('store/<int:store_id>/aisle/<int:aisle_id>/delete/', views.delete_aisle, name='deleteAisle'),
    path('store/<int:store_id>/aisle/<int:aisle_id>/update/', views.update_aisle, name='updateAisle'),

    path('product/<int:product_id>/', views.product, name='product'),
    path('product/create/', views.create_product, name='createProduct'),
    path('product/new/', views.new_product, name='newProduct'),
]
