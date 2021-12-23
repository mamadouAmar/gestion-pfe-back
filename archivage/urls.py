from django.urls import path
from archivage.views import getOneRapport, rapport, commentaires


urlpatterns = [
    path('rapport/', rapport, name="rapports"),
    path('commantaires/', commentaires, name="commentaires"),
    path('rapport/<int:pk>', getOneRapport, name="rapport")
]