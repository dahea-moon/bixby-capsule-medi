from django.urls import path
from . import views

app_name = 'pharmacy'

urlpatterns = [
    path('collectdata/', views.collectdata, name='collect_data')
]
