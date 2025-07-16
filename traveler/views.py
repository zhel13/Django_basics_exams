from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from traveler.forms import ProfileCreate, ProfileDetailForm, ProfileUpdateForm
from traveler.models import Traveler
from traveler.utils import get_traveler


class CreateTravelerView(CreateView):
    # Model and fields in Create view are only needed to create a form. If form created already we can use form_class
    # model = Traveler
    # fields = '__all__'
    form_class = ProfileCreate
    template_name = 'traveler_html/create-traveler.html'
    success_url = reverse_lazy('all-trips')


class TravelerDetailView(DetailView):
    model = get_traveler()
    template_name = 'traveler_html/details-traveler.html'


    def get_object(self, queryset=None):
        return get_traveler()

class TravelerEditView(UpdateView):

    template_name = 'traveler_html/edit-traveler.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('traveler-details')

    def get_object(self, queryset=None):
        return get_traveler()

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super().form_valid(form)

class TravelerDeleteView(DeleteView):
    model = Traveler
    template_name = 'traveler_html/delete-traveler.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_traveler()

