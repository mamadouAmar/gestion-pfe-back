from django.db import models

# Create your models here.
class User(models.Model):

    prenom = models.CharField(("prenom"), max_length=100)
    nom = models.CharField(("nom"), max_length=30)
    telephone = models.CharField(("telephone"), max_length=11)
    mail = models.EmailField(("mail"), max_length=254)
    password = models.CharField(("password"), max_length=20)

    def __str__(self):
        return self.prenom + " "+ self.nom
    
    class Meta:
        abstract = True


class Encadreur(User):

    matricule = models.CharField(("matricule"), max_length=50)

    class Meta:
        abstract = True
        verbose_name = ("Encadreur")
        verbose_name_plural = ("Encadreurs")
