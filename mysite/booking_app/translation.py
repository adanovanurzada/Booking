from .models import *
from modeltranslation.translator import translator, TranslationOptions


class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'description')



class RoomTranslationOptions(TranslationOptions):
    fields = ('room_name',)


class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)


translator.register(Hotel, HotelTranslationOptions)
translator.register(Room, RoomTranslationOptions)
translator.register(Review, ReviewTranslationOptions)
