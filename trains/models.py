from django.db import models
from django.utils import timezone
from screenings.models import Screening

# Create your models here.


class Train(models.Model):
    title = models.CharField(max_length=32, null=False, blank=False)
    description_of_direction = models.TextField(null=False, blank=False)
    start_of_the_trip = models.DateField(null=False, blank=False, default=timezone.now)
    end_of_the_trip = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return f'{self.title}'

    def get_sessions_count(self):
        return Screening.objects.filter(poezd_id__id=self.id).filter(time__gt=timezone.now()).count()