from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from traveler.utils import get_traveler
from index.views import ContextMixin
from trips.forms import CreateTripForm, UpdateTripForm, DeleteTripForm
from trips.models import Trip
from trips.utils import get_trips


def create_trip(request):
    traveler = get_traveler()
    form = CreateTripForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        trip = form.save(commit=False)
        trip.traveler = traveler
        form.save()

        return redirect('all-trips')

    context = {
        'traveler': traveler,
        'form': form,
    }

    return render(request, template_name='trip_html/create-trip.html', context=context)


class TripDetailView(ContextMixin ,DetailView):
    model = Trip
    template_name = 'trip_html/details-trip.html'
    context_object_name = 'trip'

class EditTripView(ContextMixin,UpdateView):
    queryset = get_trips()
    form_class = UpdateTripForm
    template_name = 'trip_html/edit-trip.html'
    success_url = reverse_lazy('all-trips')
    context_object_name = 'form'


class DeleteTripView(ContextMixin,DeleteView):
    model = Trip
    form_class = DeleteTripForm
    template_name = 'trip_html/delete-trip.html'
    success_url = reverse_lazy('all-trips')

    def get_initial(self):
        return self.object.__dict__


        


