from django.contrib import admin
from etude.models import Professeur, Soutenant, ProjetFinDetudes, Etudiant, Competence, Departement

# Register your models here.

admin.site.register(Professeur)

admin.site.register(ProjetFinDetudes)

admin.site.register(Competence)

admin.site.register(Departement)

admin.site.register(Soutenant)

admin.site.register(Etudiant)