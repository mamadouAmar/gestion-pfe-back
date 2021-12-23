from rest_framework import serializers

from etude.models import Competence, Departement, Etudiant, Professeur, ProjetFinDetudes, Soutenant


class DepartementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departement
        fields = "__all__"



class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = "__all__"



class ProjetFinDetudesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjetFinDetudes
        fields = "__all__"


class SoutenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soutenant
        fields = "__all__"


class EtudiantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etudiant
        fields = "__all__"


class CompetenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competence
        fields = "__all__"