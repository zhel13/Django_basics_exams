from django.urls import path, include

from trips import views

urlpatterns = [
    path('create/', views.create_trip, name='create-trip'),
    path('trip_<int:pk>/', include([
        path('details/', views.TripDetailView.as_view(), name='trip-details'),
        path('edit/', views.EditTripView.as_view(), name='trip-edit'),

        path('delete/', views.DeleteTripView.as_view(), name='trip-delete'),
    ]))

]