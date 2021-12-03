from rest_framework import serializers

from etude.models import Competence, Departement, Etudiant, Professeur, ProjetFinDetudes, Soutenant


class DepartementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departement
        fields = all



class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = all



class ProjetFinDetudesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjetFinDetudes
        fields = all


class SoutenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soutenant
        fields = all


class EtudiantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etudiant
        fields = all


class CompetenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competence
        fields = all