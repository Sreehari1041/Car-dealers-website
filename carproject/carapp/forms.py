from django import forms

from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': DateInput(),
            
        }
        labels = {
           'c_name':'customer Name',
           'case_phone':'Phone Number',
           'c_email':'Email',
           
           'car_name':'Car Name',
           'booking_date':'Booking Date',
        }