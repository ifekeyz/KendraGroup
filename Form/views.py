from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Forms

# Create your views here.
def form(request):
     if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        dateofbirth = request.POST['dateofbirth']
        occupation = request.POST['occupation']
        location = request.POST['location']

        form = Forms(name=name,email=email,address=address,phone=phone,dateofbirth=dateofbirth,occupation=occupation,location=location)
        form.save()
        messages.success(request, 'Your request has been submitted')
        return redirect('about')
    # return render(request, 'contacts/contacts.html')