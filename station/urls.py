"""
URL configuration for station project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(("trains.urls", "trains"), namespace="trains")),
#     # path('trains/', include(('trains.urls', 'trains'), namespace='trains')),

#     path('users/', include(('users.urls', 'users'), namespace="users")),
#     path('tickets/', include(('tickets.urls', 'tickets'), namespace='tickets')),
#     path('screenings/', include(('screenings.urls', 'screenings'), namespace='screenings'))
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('trains.urls', 'trains'), namespace='trains')),
    path('user/', include(('users.urls', 'users'), namespace='users')),
    path('tickets/', include(('tickets.urls', 'tickets'), namespace='tickets')),
    path('screenings/', include(('screenings.urls', 'screenings'), namespace='screenings'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
