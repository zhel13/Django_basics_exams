from django.views.generic import TemplateView, ListView

from traveler.utils import get_traveler
from trips.utils import get_trips

class AllTrips(ListView):
    queryset = get_trips()
    context_object_name = 'trips'
    template_name = 'all-trips.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler()
        return context


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler()
        return context

