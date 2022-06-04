from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/', include('log.urls')),
    path('', RedirectView.as_view(url='log/')),
    path('user/', include('django.contrib.auth.urls')),
]
