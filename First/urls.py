from django.urls import path

from . import views

urlpatterns = [
    path('first/', views.first),
    path('sendPostFirst/', views.sendPostFirst)
]
