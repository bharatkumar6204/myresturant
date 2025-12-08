from django.db import models

# Create your models here.

class Booking(models.Model):
    ct_name=models.CharField(max_length=100)
    ct_phone=models.CharField(max_length=20)
    ct_guests=models.IntegerField()
    ct_date=models.DateField()
    ct_time=models.TimeField()
    ct_request=models.TextField(blank=True)

    def __str__(self):
        return self.ct_name


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email