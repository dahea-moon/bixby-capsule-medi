from django.urls import path
from . import views

app_name = 'moonlight'

urlpatterns = [
    # path('search-nearest/<str:longt>/<str:langt>/<str:time>/', views.search_nearest, name='search_nearest')
    path('collectdata/', views.collectdata, name='collect_data')
]
