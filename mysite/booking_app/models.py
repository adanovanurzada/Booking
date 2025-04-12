from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

ROLE_CHOICES = (
    ('client', 'client'),
    ('owner', 'owner'),
    ('admin', 'admin')
)

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    full_name = models.CharField(max_length=34)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(65)], null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Hotel(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='hotels')
    hotel_name = models.CharField(max_length=100)
    description = models.TextField()
    hotel_image = models.ImageField(upload_to='hotels/', null=True, blank=True)


    def __str__(self):
        return self.hotel_name


class HotelImage(models.Model):
        hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
        image = models.ImageField(upload_to='hotel_images/')

        def __str__(self):
            return f"{self.hotel.hotel_name} Image"


STATUS_CHOICES = (
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('occupied', 'Occupied'),
)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_name = models.CharField(max_length=32)
    number = models.CharField(max_length=20)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='available')
    image = models.ImageField(upload_to='rooms/', null=True, blank=True)

    def __str__(self):
        return f"{self.hotel.hotel_name}, {self.room_name}"



class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.client.username}, {self.room.room_name}"


class Review(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

    class Meta:
        unique_together = ('client', 'hotel')



