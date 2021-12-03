from rest_framework import serializers

from entreprise.models import Employe, Entreprise


class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = all


class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = all
