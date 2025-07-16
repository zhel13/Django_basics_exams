from django.urls import path, include

from traveler import views

urlpatterns = [
    path('create/', views.CreateTravelerView.as_view(), name='create'),
    path('details/', views.TravelerDetailView.as_view(), name='traveler-details'),

    path('edit/', views.TravelerEditView.as_view(), name='traveler-edit'),

    path('delete/', views.TravelerDeleteView.as_view(), name='traveler-delete'),

]