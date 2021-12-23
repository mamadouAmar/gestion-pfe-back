from rest_framework import serializers

from entreprise.models import Employe, Entreprise


class EmployeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employe
        fields = "__all__"


class EntrepriseSerializer(serializers.ModelSerializer):

    employe = EmployeSerializer()

    class Meta:
        model = Entreprise
        fields = ["__all__", "employe"]

