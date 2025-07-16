from django.urls import path

from index import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('all-trips/', views.AllTrips.as_view(), name='all-trips'),
]