from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Houserent
from Pages.models import Team
# Create your views here.
def index(request):
    houserents = Houserent.objects.order_by('-listingDate')
    paginator = Paginator(houserents,4)
    page = request.GET.get('page')
    paged_houserents = paginator.get_page(page)

    context = {
        'houserents':paged_houserents
    }
    return render(request, 'houserent/houserents.html', context)

def houserent(request, houserent_id):
    houserent = get_object_or_404(Houserent, pk=houserent_id)
    teams = Team.objects.order_by('-hire_date').filter(is_mvp=True)[:4]

    context = {
        'houserent':houserent,
        'teams':teams
    }
    return render(request, 'houserent/houserent.html',context)