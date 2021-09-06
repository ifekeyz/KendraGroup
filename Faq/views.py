from django.shortcuts import render, redirect
from .models import FAQs, Message
from django.contrib import messages

# Create your views here.
def index(request):
    faqs = FAQs.objects.all()


    context = {
        'faqs':faqs
    }
    return render(request, 'faq/faq.html',context)


def message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        message = Message(name=name, email=email,subject=subject, message=message)
        message.save()

        messages.success(request, 'Your request has been recieved, a team member will get back')
        return redirect ('about')


