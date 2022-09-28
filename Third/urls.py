from django.urls import path

from . import views

urlpatterns = [
    path('third/', views.third),
]
