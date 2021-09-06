from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Automobile
from Pages.models import Team


# Create your views here.
def index(request):
    automobiles = Automobile.objects.order_by('-listingDate')
    paginator = Paginator(automobiles,4)
    page = request.GET.get('page')
    paged_automobiles = paginator.get_page(page)

    context = {
        'automobiles':paged_automobiles
    }
    return render(request, 'auto/automobiles.html', context)

def automobile(request, automobile_id):
    teams = Team.objects.order_by('-hire_date').filter(is_mvp=True)[:4]
    automobile = get_object_or_404(Automobile, pk=automobile_id)

    context = {
        'automobile':automobile,
        'teams':teams
    }
    return render(request, 'auto/automobile.html', context)