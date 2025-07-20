from django.views.generic import TemplateView, ListView

from traveler.utils import get_traveler
from trips.utils import get_trips

class ContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler()
        return context


class AllTrips(ContextMixin, ListView):
    queryset = get_trips()
    context_object_name = 'trips'
    template_name = 'all-trips.html'


class IndexView(ContextMixin, TemplateView):
    template_name = 'index.html'


