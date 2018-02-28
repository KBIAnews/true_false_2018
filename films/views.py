from django.shortcuts import render, get_object_or_404
from bakery.views import BuildableDetailView, BuildableListView

from .models import Film, Screening, Venue

# Create your views here.

class FilmListView(BuildableListView):
    queryset = Film.objects.all()
    model = Film

class FilmDetailView(BuildableDetailView):
    model = Film
    template_name = 'films/film_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FilmDetailView, self).get_context_data(**kwargs)

        # Now Try to Get Screenings
        film_scratch = self.object
        context['screenings_list'] = Screening.objects.filter(film=film_scratch)
        context['film_scratch'] = film_scratch
        return context

class VenueDetailView(BuildableDetailView):
    model = Venue
    template_name = 'films/venue_detail.html'

    def get_context_data(self, **kwargs):
        context = super(VenueDetailView, self).get_context_data(**kwargs)

        # Now Try to Get Screenings
        venue_scratch = self.object
        context['screenings_list'] = Screening.objects.filter(venue=venue_scratch)
        return context