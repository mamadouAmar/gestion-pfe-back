from django.urls import path

from etude.views import competence, departement, etudiant, professeur, projetFinDetudes, soutenant

urlpatterns = [
    path('departement/', departement, name="departement"),
    path('professeur/', professeur, name="professeur"),
    path('competence/', competence, name="competence"),
    path('projetFinDetudes/', projetFinDetudes, name="PFE"),
    path('etudiant/', etudiant, name="etudiant"),
    path('soutenant/', soutenant, name="soutenant")
]