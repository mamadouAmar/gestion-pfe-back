from django.db import models

from user.models import Encadreur

# Create your models here.
class Entreprise(models.Model):
    nom = models.CharField(("intitule"), max_length=256)
    identifiant = models.CharField(("identifiant"), max_length=50)
    pays = models.CharField(("pays"), max_length=50)
    ville = models.CharField(("ville"), max_length=50)
    addresse = models.CharField(("addresse"), max_length=50)
    debut_partanariat = models.DateField(("debut partenariat"), auto_now=False, auto_now_add=False, null=True, blank=True)
    fin_partenariat = models.DateField(("fin partenariat"), auto_now=False, auto_now_add=False, null=True)

    class Meta:
        verbose_name = ("Entreprise")
        verbose_name_plural = ("Entreprises")

    def __str__(self):
        return self.nom


class Employe(Encadreur):

    poste = models.CharField(("poste"), max_length=100)
    entreprise =  models.ForeignKey(Entreprise, verbose_name=("entreprise"), on_delete=models.CASCADE)    

    class Meta:
        verbose_name = ("Employe")
        verbose_name_plural = ("Employes")