from django.urls import path
from . import views
    # store/urls.py
urlpatterns = [
    path("", views.store, name="store"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("checkout/<int:pk>/", views.checkout, name="checkout"),
    path("order/success/", views.order_sucess, name="order/success"),
    path("category/<int:category_id>/", views.category_products, name="category_products"),
    

    



]
