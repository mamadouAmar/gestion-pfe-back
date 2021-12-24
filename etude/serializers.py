from django.db.models import manager
from rest_framework import serializers
from entreprise.serializers import EntrepriseSerializer

from etude.models import Competence, Departement, Etudiant, Professeur, ProjetFinDetudes, Soutenant
from user.serializers import EncadreurSerializer


class DepartementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departement
        fields = "__all__"


class CompetenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competence
        fields = "__all__"


class ProfesseurSerializer(serializers.ModelSerializer):
    
    departement = DepartementSerializer()

    class Meta:
        model = Professeur
        fields = "__all__"



class ProjetFinDetudesSerializer(serializers.ModelSerializer):

    departement = DepartementSerializer(read_only=True)
    encadreurs = EncadreurSerializer(read_only=True, many=True)
    competences = CompetenceSerializer(read_only=False, many=True)
    entreprise = EntrepriseSerializer(read_only=True)

    class Meta:
        model = ProjetFinDetudes
        fields = "__all__"


class SoutenantSerializer(serializers.ModelSerializer):

    departement = DepartementSerializer(read_only=True)
    projet = ProjetFinDetudesSerializer(read_only=True)

    class Meta:
        model = Soutenant
        fields = "__all__"


class EtudiantSerializer(serializers.ModelSerializer):

    competences = CompetenceSerializer(read_only=True, many=True)

    class Meta:
        model = Etudiant
        fields = "__all__"
