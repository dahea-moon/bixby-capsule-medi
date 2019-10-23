from django.urls import path
from . import views

app_name = 'anal'

urlpatterns = [
    path('collectdata/', views.collectdata, name='collect_data')
]
