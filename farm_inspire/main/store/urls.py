from django.urls import path

from . import views
urlpatterns = [
       
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('', views.storeproduct, name="storeProd"),


]