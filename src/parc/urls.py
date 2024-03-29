from django.urls import path
from parc.views import ParcCreate, ParcHome, search_parc

app_name = "parc"

urlpatterns = [
    path('', ParcHome.as_view(), name='home'),
    path('create/', ParcCreate.as_view(), name='create'),
    path('search/', search_parc, name='search')
]