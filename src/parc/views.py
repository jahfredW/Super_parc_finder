from django.shortcuts import render
from parc.models import Adress
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from parc.models import Parc

# Create your views here.



def parc(request):
    adresse = Adress.adress
    return render(request, 'parc/parc.html', context= { 'adresse' : adresse})

class ParcCreate(CreateView):
    model = Parc
    template_name = "parc/parc_create.html"
    fields = ['title', 'content', ]