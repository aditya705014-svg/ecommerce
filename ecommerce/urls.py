from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),

    path("accounts/", include("accounts.urls")),
    path("store/", include("store.urls")),
]

# root ("/") par sidha login bhejna
urlpatterns += [
    path("", lambda request: redirect("login")),
]