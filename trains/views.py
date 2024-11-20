from django.shortcuts import render
from trains.models import Train
from django.http import Http404

# App services
from trains.services.get_current_and_next_trains import get_current_and_next_trains


# Create your views here.

def active_trains_list(request):
    context = dict()
    context['current_trains'], context['next_trains'] = get_current_and_next_trains()
    return render(request, 'trains/active_list.html', context)


def train_page(request, train_id):
    try:
        train = Train.objects.get(id=train_id)
        return render(request, 'trains/train_page.html', {'train': train})
    except Train.DoesNotExist:
        raise Http404
