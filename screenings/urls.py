from django.urls import path
import screenings.views as views

urlpatterns = [
    path('schedule/', views.screenings_schedule, name='schedule'),
    path('schedule/<int:train>/', views.movie_screenings_schedule, name='train_schedule')
]