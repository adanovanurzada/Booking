from django_filters import FilterSet
from .models import *


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'hotel_name': ['exact'],
        }


class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_name': ['exact'],
            'status': ['exact'],
        }


class BookingFilter(FilterSet):
    class Meta:
        model = Booking
        fields = {
            'start_date': ['gte', 'lte'],
            'end_date': ['gte', 'lte'],
        }
