from django.urls import path

from .views import UserDetailView, UserUpdateView, UserCreateView, UserDeleteView

urlpatterns = [
    path('profile/<uuid:pk>', UserDetailView.as_view(), name='user_detail'),
    path('profile/<uuid:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('profile/<uuid:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('profile/create', UserCreateView.as_view(), name='user_create'),
]

