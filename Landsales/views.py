from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Landsale
from Pages.models import Team

# Create your views here.
def index(request):
    landsales = Landsale.objects.order_by('-listingDate')
    paginator = Paginator(landsales,4)
    page = request.GET.get('page')
    paged_landsales = paginator.get_page(page)

    context = {
        'landsales':paged_landsales
    }
    return render(request, 'landsale/landsales.html', context)

def landsale(request, landsale_id):
    landsale = get_object_or_404(Landsale, pk=landsale_id)
    teams = Team.objects.order_by('-hire_date').filter(is_mvp=True)[:4]

    context = {
        'landsale':landsale,
        'teams':teams
    }
    return render(request, 'landsale/landsale.html', context)