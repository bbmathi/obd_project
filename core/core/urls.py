# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
            # Django admin route
    path("", include("authentication.urls")),
    path('admin/', admin.site.urls),  # Auth routes - login / register
    path("", include("app.urls")),
     ]

