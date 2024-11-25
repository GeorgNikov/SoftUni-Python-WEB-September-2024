from django.contrib import admin
from django.urls import path, include

from WoSApp.common.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('car/', include('WoSApp.cars.urls')),
    path('profile/', include('WoSApp.profiles.urls')),
]
