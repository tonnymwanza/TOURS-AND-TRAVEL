from django.contrib import admin

from . models import Contact
from . models import Trending
from . models import Booking
# Register your models here.

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'subject',
        'message'
    ]

@admin.register(Booking)
class AdminBooking(admin.ModelAdmin):
    list_display = [
        'destination',
        'check_in',
        'check_out',
        'adults',
        'children'
    ]

@admin.register(Trending)
class AdminTrending(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'location',
        'image'
    ]