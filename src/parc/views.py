from django.shortcuts import render
from django.shortcuts import HttpResponse
from parc.models import Adress
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from parc.models import Location

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

        return queryset.filter(published=True)


class ParcCreate(CreateView):
    model = Location
    template_name = "parc/parc_create.html"
    context_object_name = 'location'
    fields = ['name']


class ParcList(ListView):
    model = Location
    template_name = 'parc/derniers_parc.html'
    context_object_name = 'location'
    fields = '__all__'


def search_parc(request):

    queryset = Location.objects.all()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            recherche = form.cleaned_data['adress']

            return render(request, 'parc/list.html', context={'form': form, 'queryset': queryset, 'recherche': recherche})


    else:
        form = SearchForm()

    return render(request, 'parc/search.html', {'form': form })
