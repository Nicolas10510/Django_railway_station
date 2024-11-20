from dataclasses import dataclass

from django.utils import timezone

from trains.models import Train
from screenings.models import Screening


@dataclass
class ValidTrainScreenings:
    train: Train
    screenings: list[Screening]
    screenings_time: list[str]


def get_valid_train_screenings_with_time(train_id: int) -> ValidTrainScreenings:
    train = Train.objects.get(pk=train_id)
    screenings = Screening.objects.filter(poezd_id=train.id).order_by('-time').filter(time__gt=timezone.now())
    screenings_time = list(set(map(lambda x: x[0].date(), screenings.values_list('time'))))

    return ValidTrainScreenings(train=train, screenings=screenings, screenings_time=screenings_time)
