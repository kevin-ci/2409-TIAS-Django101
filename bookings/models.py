from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    number_of_people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField()

class BookingSlot(models.Model):
    booked = models.BooleanField(default=False)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name="bookingslots"
    )

    def __str__(self):
        return f"{self.date}; {self.time}"