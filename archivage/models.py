from django.db import models
from django.db.models.fields.related import ForeignKey

from etude.models import Etudiant, ProjetFinDetudes, Soutenant
from user.models import User

# Create your models here.
class Rapport(models.Model):
    projet = models.ForeignKey(ProjetFinDetudes, verbose_name=("PFE"), on_delete=models.CASCADE)
    auteur = models.ForeignKey(Soutenant, verbose_name=("soutenant"), on_delete=models.CASCADE)
    date = models.DateTimeField(("date d'archivage"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = ("Rapport")
        verbose_name_plural = ("Rapports")

    def __str__(self):
        return str(self.projet) + " par " + str(self.auteur)


class Commentaires(models.Model):
    rapport = models.ForeignKey(Rapport, verbose_name=("rapport"), on_delete=models.CASCADE)
    auteur = models.ForeignKey(Etudiant, verbose_name=("auteur"), on_delete=models.CASCADE)
    date = models.DateTimeField(("date"), auto_now=False, auto_now_add=False)
    commentaire = models.CharField(("commentaire"), max_length=256)

    class Meta:
        verbose_name = ("Commentaires")
        verbose_name_plural = ("Commentairess")

    def __str__(self):
        return self.commentaire