from django.shortcuts import render
from .models import Slider
from Automobiles.models import Automobile
from Houserents.models import Houserent
from Housesales.models import Housesale
from Landsales.models import Landsale
from .models import Team
from Subscrib.forms import EmailSignupForm

# Create your views here.
def index(request):
    automobiles = Automobile.objects.order_by('listingDate')[:4]
    housesales = Housesale.objects.order_by('listingDate')[:4]
    houserents = Houserent.objects.order_by('listingDate')[:4]
    landsales = Landsale.objects.order_by('listingDate')[:4]
    teams = Team.objects.order_by('hire_date')[:5]
    sliders = Slider.objects.filter(is_published=True)[:3]
    form = EmailSignupForm()

    context ={
        'sliders':sliders,
        'automobiles':automobiles,
        'housesales':housesales,
        'houserents':houserents,
        'landsales':landsales,
        'teams':teams,
        'form':form
    }
    return render(request, 'Pages/index.html', context)

def about(request):
    sliders = Slider.objects.filter(is_published=True)[:3]

    context = {
        'sliders':sliders
    }
    return render(request, 'Pages/about.html', context)