from django.urls import path

from . import views

urlpatterns = [
    path('third/', views.third),
    path('responseFile/', views.responseFile),
]
