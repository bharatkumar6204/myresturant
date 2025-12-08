from django.contrib import admin
from app1.models import Booking
from app1.models import Newsletter
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ['ct_name','ct_phone','ct_guests','ct_date','ct_time','ct_request']

admin.site.register(Booking, BookingAdmin)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['id','email','subscribed_at']

admin.site.register(Newsletter,NewsletterAdmin)