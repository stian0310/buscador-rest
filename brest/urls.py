from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('APIv1/', include('API.urls')),
    path('lomasbuscado/', include('bapp.urls'))
]
