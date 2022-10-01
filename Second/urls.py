from django.urls import path

from . import views

urlpatterns = [
    path('second/', views.second),
    path('sendPostSecond/', views.sendPostSecond),
    path('upload_detail/', views.upload_detail),
    # path('detail/', views.detail),
]
