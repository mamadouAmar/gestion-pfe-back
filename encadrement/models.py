from django.db import models

from etude.models import ProjetFinDetudes
from user.models import User

# Create your models here.
class Reunion(models.Model):
    sujet = models.CharField(("sujet"), max_length=256)
    date = models.DateTimeField(("date et heure"), auto_now=False, auto_now_add=False)
    lieu = models.CharField(("lieu"), max_length=100)
    rapport = models.TextField(("resume"))
    compte_rendu = models.FileField(("compte rendu"), upload_to=None, max_length=100)
    projet = models.ForeignKey(ProjetFinDetudes, verbose_name=("PFE"), on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, verbose_name=("participants"))

    class Meta:
        verbose_name = ("Reunion")
        verbose_name_plural = ("Reunions")

    def __str__(self):
        return self.sujet

    def get_absolute_url(self):
        return reverse("Reunion_detail", kwargs={"pk": self.pk})


class Message(models.Model):
    objet = models.CharField(("objet"), max_length=50)
    contenu = models.CharField(("contenu"), max_length=500)
    date = models.DateTimeField(("date"), auto_now=False, auto_now_add=False)
    auteur = models.ForeignKey(User, verbose_name=("auteur"), on_delete=models.CASCADE)
    projet = models.ForeignKey(ProjetFinDetudes, verbose_name=("projet"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    def __str__(self):
        return self.objet

    def get_absolute_url(self):
        return reverse("Message_detail", kwargs={"pk": self.pk})
