from django.db import models
from django.db.models.base import Model

from etude.models import ProjetFinDetudes, Soutenant
from user.models import Encadreur

# Create your models here.
class Jury(models.Model):
    membres = models.ManyToManyField(Encadreur, verbose_name=("membres"))
    
    class Meta:
        verbose_name = ("Jury")
        verbose_name_plural = ("Jurys")


class Soutenance(models.Model):
    projet = models.ForeignKey(ProjetFinDetudes, verbose_name=("PFE"), on_delete=models.CASCADE)
    jury = models.OneToOneField(Jury, verbose_name=("jury"), on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(("date"), auto_now=False, auto_now_add=False)
    lieu  = models.CharField(("lieu"), max_length=50)
    acces = models.CharField(("acces"), max_length=50)
    rapport_soutenance = models.FileField(("rapport soutenance"), upload_to=None, max_length=100, null=True, blank=True)
    resume = models.TextField(("resume soutenance"), null=True, blank=True)

    class Meta:
        verbose_name = ("Soutenance")
        verbose_name_plural = ("Soutenances")

    def __str__(self):
        return "Soutenance "+str(self.projet)


class Appreciations(models.Model):
    remarques = models.CharField(("remarques"), max_length=500, null=True)
    appreciations = models.CharField(("appreciation"), max_length=100, null=True)
    suggestions = models.CharField(("suggestions"), max_length=500, null=True)
    note = models.PositiveSmallIntegerField(("note"))
    soutenant = models.ForeignKey(Soutenant, verbose_name=("soutenant"), on_delete=models.CASCADE)
    jury = models.ForeignKey(Jury, verbose_name=("jury"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Appreciations")
        verbose_name_plural = ("Appreciations")