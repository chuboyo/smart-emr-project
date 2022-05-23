from django.urls import path

from .views import *

urlpatterns = [
    path('profile/<uuid:pk>', UserDetailView.as_view(), name='user_detail'),
    path('profile/<uuid:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
]