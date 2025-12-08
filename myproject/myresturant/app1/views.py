from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Booking
from .models import Newsletter
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def booktable(request):
    return render(request, 'book_table.html')

def save_form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        guests=request.POST.get('guests')
        date=request.POST.get('date')
        time=request.POST.get('time')
        req_uest=request.POST.get('request')
        # Save to DB
        my_model=Booking(ct_name=name,ct_phone=phone,ct_guests=guests,ct_date=date,ct_time=time,ct_request=req_uest)
        my_model.save()
        return HttpResponse("🎉 Your table has been booked successfully! We are waiting to serve you ❤️")

def newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        Newsletter.objects.create(email=email)
        messages.success(request, "Subscribed Successfully!")
        return redirect('/')