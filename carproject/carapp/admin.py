from django.contrib import admin
from .models import cars,Booking

# Register your models here.

admin.site.register(cars)


class BookingAdmin(admin.ModelAdmin):
    list_display =  ( 'c_name', 'case_phone', 'c_email', 'car_name','booking_date' )

admin.site.register(Booking, BookingAdmin)
