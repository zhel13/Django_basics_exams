from trips.models import Trip


def get_trips():
    return Trip.objects.all().order_by('-start_date')