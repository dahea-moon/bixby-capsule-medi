from django.urls import path
from . import views

app_name = 'total'

urlpatterns = [
    path('collectdata/', views.collectdata, name='collect_data')
]
