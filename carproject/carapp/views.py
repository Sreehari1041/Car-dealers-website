from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import cars
from .forms import BookingForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    else:
        form = BookingForm()
    
    dict_form = {'form': form}
    return render(request, 'booking.html', dict_form)

def cars_view(request):
    all_cars = cars.objects.all()  
    dict_cars = {'cars': all_cars}  
    return render(request, 'cars.html', dict_cars) 

def contact(request):
    return render(request, 'contact.html')



