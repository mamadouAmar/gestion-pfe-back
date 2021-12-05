from django.urls import path
from archivage.views import rapport, commentaires


urlpatterns = [
    path('rapport/', rapport, name="rapport"),
    path('commantaires/', commentaires, name="commentaires"),
]