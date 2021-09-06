from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Housesale
from Pages.models import Team

# Create your views here.
def index(request):
    housesales = Housesale.objects.order_by('-listingDate')
    paginator = Paginator(housesales,4)
    page = request.GET.get('page')
    paged_housesales = paginator.get_page(page)

    context = {
        'housesales':paged_housesales
    }
    return render(request, 'housesale/housesales.html', context)

def housesale(request, housesale_id):
    housesale = get_object_or_404(Housesale, pk=housesale_id)
    teams = Team.objects.order_by('-hire_date').filter(is_mvp=True)[:4]

    context = {
        'housesale':housesale,
        'teams':teams
    }
    return render(request, 'housesale/housesale.html', context)