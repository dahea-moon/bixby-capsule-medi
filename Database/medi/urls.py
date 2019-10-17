from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1/', include('AED.urls')),
    path('api/2/', include('sooyusil.urls')),
    path('api/3/', include('pharmacy.urls')),
    path('api/4/', include('emergency.urls')),
    path('api/5/', include('anal.urls')),
    path('api/6/', include('bone.urls')),
    path('api/7/', include('child.urls')),
    path('api/8/', include('dental.urls')),
    path('api/9/', include('external.urls')),
    path('api/10/', include('eye.urls')),
    path('api/11/', include('family.urls')),
    path('api/12/', include('general.urls')),
    path('api/13/', include('internal.urls')),
    path('api/14/', include('men.urls')),
    path('api/15/', include('mental.urls')),
    path('api/16/', include('moonlight.urls')),
    path('api/17/', include('nerve.urls')),
    path('api/18/', include('oriental.urls')),
    path('api/19/', include('plastic.urls')),
    path('api/20/', include('public_health.urls')),
    path('api/21/', include('skin.urls')),
    path('api/22/', include('total.urls')),
    path('api/23/', include('women.urls')),
]
