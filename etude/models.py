from django.db import models
from django.db.models.fields.related import ManyToManyField

from user.models import Encadreur, User

# Create your models here.
class Departement(models.Model):
    intitule = models.CharField(("intitule"), max_length=256)
    acronyme = models.CharField(("acronyme"), max_length=5)

    class Meta:
        verbose_name = ("Departement")
        verbose_name_plural = ("Departements")

    def __str__(self):
        return self.name


class Professeur(Encadreur):
    specialite = models.CharField(("specialite"), max_length=50)
    role = models.CharField(("role"), max_length=100)
    description = models.TextField(("description"))
    departement = models.ForeignKey(Departement, verbose_name=("departement"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Professeur")
        verbose_name_plural = ("Professeurs")


class Competence(models.Model):
    intitule = models.CharField(("intitule"), max_length=50)
    domaine = models.CharField(("domaine"), max_length=50)
    description = models.CharField(("description"), max_length=256)

    class Meta:
        verbose_name = ("Competence")
        verbose_name_plural = ("Competences")

    def __str__(self):
        return self.intitule


class ProjetFinDetudes(models.Model):
    sujet = models.CharField(("sujet"), max_length=500)
    annee_academique = models.PositiveIntegerField(("annee academique"))
    departement = models.ForeignKey(Departement, verbose_name=("departement"), on_delete=models.CASCADE)
    encadreurs = models.ManyToManyField(Encadreur, verbose_name=("encadreurs"))
    competences = models.ManyToManyField(Competence, verbose_name=("competences"))

    class Meta:
        verbose_name = ("PFE")
        verbose_name_plural = ("PFEs")

    def __str__(self):
        return self.sujet


class Etudiant(User):
    numero_etudiant = models.CharField(("numero carte etudiant"), max_length=20)
    annee_d_entree = models.DateField(("Annee d'entree"), auto_now=False, auto_now_add=False)
    departement = models.ForeignKey(Departement, verbose_name=("departement"), on_delete=models.CASCADE)
    competences = models.ManyToManyField(Competence, verbose_name=_("competences"))


    class Meta:
        verbose_name = ("Etudiant")
        verbose_name_plural = ("Etudiants")


class Soutenant(Etudiant):
    projet = models.ForeignKey(ProjetFinDetudes, verbose_name=("PFE"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Soutenant")
        verbose_name_plural = ("Soutenants")
