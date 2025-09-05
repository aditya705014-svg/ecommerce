from django.urls import path
from . import views
    # store/urls.py
urlpatterns = [
    path("", views.store, name="store"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("checkout/<int:pk>/", views.checkout, name="checkout"),
    path("order/success/", views.order_sucess, name="order/success"),
    path("category/<int:category_id>/", views.category_products, name="category_products"),
    path('cart/', views.cart, name='cart'),  
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<str:key>/', views.remove_from_cart, name='remove_from_cart'),
    path("checkout/", views.checkout_cart, name="checkout_cart"),  
    path("order/success/", views.success_cart, name="success_cart"),
    # Checkout success page
    # path("order/success/", views.success_cart, name="success_cart"),




]