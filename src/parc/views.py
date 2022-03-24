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
    fields = ['name', 'address_1', 'postal_code', 'city', 'thumbnail', 'author',]
    context_object_name = "parc"

    """
    def clean_title(self):
        adresse = self.cleaned_data['adress_1']
        if Location.objects.filter(adresse=adresse).exists():
            raise forms.ValidationError("You have already written a book with same title.")
        return adresse
    """

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
    print(queryset)

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            recherche = form.cleaned_data['adress']
            recherche = recherche.replace('é', 'e')
            print(recherche)
            # ici il y a un truc à faire.
            # on récupère recherche et on mate si il correspond avec l'adresse

        for entry in queryset:
            adress = entry.adresse()
            print(entry.name)
            print(adress)
            if recherche.lower() in adress.replace('é', 'e') or recherche.lower() in entry.name.replace('é', 'e'):
                ok = True
                break

        if ok:
            return render(request, 'parc/list.html', context={'form': form, 'queryset': queryset, 'recherche': recherche})

        else:
            return HttpResponse("Aucun resutat")

    else:
        form = SearchForm()

    return render(request, 'parc/search.html', {'form': form })
