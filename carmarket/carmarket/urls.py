from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import splash_view, search_car_brand_names

urlpatterns = [
    path('', splash_view, name='splash'),
    path('search/', search_car_brand_names, name='car_brand_names'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] 

if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)