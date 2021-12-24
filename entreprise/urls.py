from django.urls import path

from entreprise.views import employe_, entreprise, employe, entreprise_


urlpatterns = [
    path('employe/', employe, name="employes"),
    path('entreprise/', entreprise, name="entreprises"),
    path('entreprise/<int:pk>/', entreprise_, name="entreprise"),
    path('employe/<int:pk>/', employe_, name="employe")
]