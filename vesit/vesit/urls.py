from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('headAdmin/', include('headSupervisor.urls')),
    path('accounts/',include('accounts.urls')),
    path('',include('accounts.urls')),
]