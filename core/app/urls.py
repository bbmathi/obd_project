# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.urls import path, re_path
from .import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('newPost', views.newPost),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),

    path('newOBD', views.newOBD),
    path('showOBD', views.showOBD),
    path('editOBD/<int:id>', views.editOBD),
    path('deleteOBD/<int:id>', views.destroyOBD),
    path('updateOBD/<int:id>', views.updateOBD),

    path('newCar', views.newCar),
    path('showCar', views.showCar),
    path('editCar/<int:id>', views.editCar),
    path('deleteCar/<int:id>', views.destroyCar),
    path('updateCar/<int:id>', views.updateCar),
    path('dashboard', views.chart),
    path('map', views.MapView),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    re_path(r'^.*\.*', views.newPost, name='pages'),
    re_path(r'^.*\.*', views.newOBD, name='pages'),
    re_path(r'^.*\.*', views.newCar, name='pages'),
    re_path(r'^.*\.*', views.MapView,name='pages')
    ]
