

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #admin site
    path("admin/", admin.site.urls),

    #authentication
    path("account/", include('django.contrib.auth.urls')),

    path("account/", include('myapps.account.urls')),

    #entrypoint
    path("", include('myapps.cafetaria.urls')),
    path("cafeadmin/", include('cafeadmin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
