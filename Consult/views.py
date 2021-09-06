from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Consulting
# Create your views here.
def consult(request):
    if request.method=="POST":
        consulting = Consulting()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        location = request.POST.get('location')
        price = request.POST.get('price')
        message = request.POST.get('message')

        consulting.name=name
        consulting.email=email
        consulting.phone=phone
        consulting.address=address
        consulting.location=location
        consulting.price=price
        consulting.message=message
        consulting.save()
        messages.success(request, 'Your request has been submitted')
        return redirect('about')

    return render(request,'Pages/index.html')