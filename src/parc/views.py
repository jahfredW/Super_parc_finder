from django.shortcuts import render
from django.shortcuts import HttpResponse
from parc.models import Adress
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from parc.models import Location, Abus

from parc_finder.forms import SearchForm

# Create your views here.

class ParcHome(ListView):
    model = Location
    context_object_name = "parc"
    template_name = "parc/accueil.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter()


class ParcCreate(CreateView):
    model = Location
    template_name = "parc/parc_create.html"
    fields = ['name']

class AbusCreate(CreateView):
    model = Abus
    template_name = "parc/abus_form.html"
    fields = "__all__"
    context_object_name = "abus"


class ParcList(ListView):
    model = Location
    template_name = 'parc/derniers_parc.html'
    context_object_name = 'location'
    fields = '__all__'


def search_parc(request):

    ok = False
    queryset = Location.objects.all()

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            recherche = form.cleaned_data['adress']
            # ici il y a un truc à faire.
            # on récupère recherche et on mate si il correspond avec l'adresse

        for entry in queryset:
            adress = entry.adresse()
            if recherche.lower() in adress or recherche.lower( ) in entry.name:
                ok = True
                break

        if ok:
            return render(request, 'parc/list.html', context={'form': form, 'queryset': queryset, 'recherche': recherche})

        else:
            return HttpResponse("Aucun resutat")

    else:
        form = SearchForm()

    return render(request, 'parc/search.html', {'form': form })
