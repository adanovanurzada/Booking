from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'full_name']


class HotelListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'description', 'hotel_image']


class HotelDetailSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Hotel
        fields = '__all__'



class RoomListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_name', 'number', 'status', 'image']


class RoomDetailSerializers(serializers.ModelSerializer):
    hotel = HotelListSerializers(read_only=True)

    class Meta:
        model = Room
        fields = '__all__'


class BookingListSerializers(serializers.ModelSerializer):
    client = UserProfileSimpleSerializers(read_only=True)
    room = RoomListSerializers(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'client', 'room', 'start_date', 'end_date']


class BookingDetailSerializers(serializers.ModelSerializer):
    client = UserProfileSimpleSerializers(read_only=True)
    room = RoomDetailSerializers(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    client = UserProfileSimpleSerializers(read_only=True)
    hotel = HotelListSerializers(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

