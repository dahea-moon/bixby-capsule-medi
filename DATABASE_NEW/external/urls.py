from django.urls import path
from . import views

app_name = 'external'

urlpatterns = [
    path('collectdata/', views.collectdata, name='collect_data')
]
