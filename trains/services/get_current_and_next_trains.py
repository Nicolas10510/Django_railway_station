from trains.models import Train
from django.utils import timezone


def get_current_and_next_trains() -> tuple[list[Train], list[Train]]:
    current_trains = Train.objects.filter(start_of_the_trip__lt=timezone.now(), end_of_the_trip__gt=timezone.now()).order_by('-start_of_the_trip')
    next_trains = Train.objects.filter(start_of_the_trip__gt=timezone.now()).order_by('start_of_the_trip')

    return current_trains, next_trains