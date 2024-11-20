from django.urls import path
import trains.views as views

urlpatterns = [
    path('', views.active_trains_list, name='index'),
    path('train/<int:train_id>/', views.train_page, name='train_page')
]