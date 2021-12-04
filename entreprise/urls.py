from django.urls import path

from entreprise.views import entreprise, employe


urlpatterns = [
    path('employe/', employe, name="employe"),
    path('entreprise/', entreprise, name="entreprise"),
]