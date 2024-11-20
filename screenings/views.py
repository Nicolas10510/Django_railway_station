from django.shortcuts import render

# App services
from screenings.services.get_valid_screenings_with_time import get_valid_screenings_with_time
from screenings.services.get_valid_screenings_with_time_by_train import get_valid_train_screenings_with_time


def screenings_schedule(request):

    screenings = get_valid_screenings_with_time()
    context = {
        'screenings': screenings.screenings,
        'time': screenings.screenings_time
    }

    return render(request, 'screenings/schedule.html', context)


def movie_screenings_schedule(request, train):
    valid_screenings = get_valid_train_screenings_with_time(train)

    context = {
        'train': valid_screenings.train,
        'screenings': valid_screenings.screenings,
        'time': valid_screenings.screenings_time
    }

    return render(request, 'screenings/train_schedule.html', context)
