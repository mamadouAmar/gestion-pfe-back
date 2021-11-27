from django.db import models

from user.models import Encadreur

# Create your models here.

class Professeur(Encadreur):

    specialite = models.CharField(("specialite"), max_length=50)
    role = models.CharField(("role"), max_length=100)
    description = models.TextField(("description"))
    

    class Meta:
        verbose_name = ("Professeur")
        verbose_name_plural = ("Professeurs")