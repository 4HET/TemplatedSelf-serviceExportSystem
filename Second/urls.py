from django.urls import path

from . import views

urlpatterns = [
    path('second/', views.second),
    path('sendPostSecond/', views.sendPostSecond),
    path('upload_detail/', views.upload_detail),
    path('detail/', views.detail),
    path('deviate/', views.deviate),
    path('impl/', views.impl),
    path('downloadDetail/', views.downloadDetail),
    path('downloadDevite/', views.downloadDevite),
    path('downloadImpl/', views.downloadImpl),

]
