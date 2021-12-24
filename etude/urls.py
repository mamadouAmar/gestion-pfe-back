from django.urls import path

from etude.views import *

urlpatterns = [
    path('departement/', departement, name="departements"),
    path('professeur/', professeur, name="professeurs"),
    path('competence/', competence, name="competences"),
    path('projetFinDetudes/', projetFinDetudes, name="PFEs"),
    path('etudiant/', etudiant, name="etudiants"),
    path('soutenant/', soutenant, name="soutenants"),
    path('departement/<int:pk>/', departement_, name="departement"),
    path('professeur/<int:pk>/', professeur_, name="professeur"),
    path('competence/<int:pk>/', competence_, name="competence"),
    path('projetFinDetudes/<int:pk>/', projetFinDetudes_, name="PFE"),
    path('etudiant/<int:pk>/', etudiant_, name="etudiant"),
    path('soutenant/<int:pk>/', soutenant_, name="soutenant")
]