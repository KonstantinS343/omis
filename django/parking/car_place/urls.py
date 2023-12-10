from django.urls import path

from .views import LoginInterface, RegisterInterface, UserInterface
from .views_admin import AdminInterface


user_urls = [
    path('user/<int:pk>/', UserInterface.as_view(), name='user'),
    path('user/<int:pk>/create/', UserInterface.as_view(), name='user_create'),
    path('user/<int:pk>/history/', UserInterface.as_view(), name='user_history'),
    path('user/<int:pk>/place/<int:place_pk>', UserInterface.as_view(), name='user_history_details'),
    path('user/<int:pk>/place/<int:place_pk>/detail', UserInterface.as_view(), name='user_history_details'),
    path('user/<int:pk>/place/<int:place_pk>/delete', UserInterface.as_view(), name='user_history_delete'),
    path('user/<int:pk>/place/<int:place_pk>/update', UserInterface.as_view(), name='user_history_update'),
]

admin_urls = [
    path('admin/<int:pk>/', AdminInterface.as_view(), name='admin'),
    path('admin/<int:pk>/create/', AdminInterface.as_view(), name='admin_create'),
    path('admin/<int:pk>/places/', AdminInterface.as_view(), name='admin_place'),
    path('admin/<int:pk>/place/<int:place_pk>', AdminInterface.as_view(), name='admin_place_details'),
    path('admin/<int:pk>/place/<int:place_pk>/detail', AdminInterface.as_view(), name='admin_place_details'),
    path('admin/<int:pk>/place/<int:place_pk>/delete', AdminInterface.as_view(), name='admin_place_delete'),
    path('admin/<int:pk>/place/<int:place_pk>/update', AdminInterface.as_view(), name='admin_place_update'),
]

urlpatterns = [
    path('register/', RegisterInterface.as_view(), name='register'),
    path('login/', LoginInterface.as_view(), name='login'),
] + user_urls + admin_urls
