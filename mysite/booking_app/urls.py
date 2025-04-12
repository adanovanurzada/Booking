from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'review', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('hotels/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),

    path('rooms/', RoomListAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),

    path('bookings/', BookingListAPIView.as_view(), name='booking_list'),
    path('bookings/<int:pk>/', BookingDetailAPIView.as_view(), name='booking_detail'),

]