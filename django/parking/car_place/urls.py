from django.urls import path

from .views import LoginInterface, RegisterInterface, HomeInterface, UserInterface

urlpatterns = [
    path('register/', RegisterInterface.as_view(), name='register'),
    path('login/', LoginInterface.as_view(), name='login'),
    path('home/', HomeInterface.as_view(), name='home'),
    path('user/<int:pk>/', UserInterface.as_view(), name='user'),
    path('user/<int:pk>/create/', UserInterface.as_view(), name='user_create'),
    path('user/<int:pk>/history/', UserInterface.as_view(), name='user_history'),
    path('user/<int:pk>/place/<int:place_pk>', UserInterface.as_view(), name='user_history_details'),
    path('user/<int:pk>/detail/<int:place_pk>', UserInterface.as_view(), name='user_history_details'),
    path('user/<int:pk>/place/<int:place_pk>/delete', UserInterface.as_view(), name='user_history_delete'),
    path('user/<int:pk>/place/<int:place_pk>/update', UserInterface.as_view(), name='user_history_update'),
]
