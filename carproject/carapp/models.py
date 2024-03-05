from django.db import models

# Create your models here.

        
class cars(models.Model):
    car_name=models.CharField(max_length=255)
    car_year=models.IntegerField()
    
    car_image=models.ImageField(upload_to='static/cars')
    car_price=models.IntegerField(max_length=10)
   
    def __str__(self):
        return self.car_name
    
class Booking(models.Model):
    c_name = models.CharField(max_length=255)
    case_phone = models.CharField(max_length=10)
    c_email = models.EmailField()
    car_name = models.ForeignKey(cars, on_delete=models.CASCADE)
    booking_date = models.DateField()
    
