from rest_framework import serializers

from entreprise.models import Employe, Entreprise


class EmployeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employe
        fields = "__all__"


class EntrepriseSerializer(serializers.ModelSerializer):

    employes = EmployeSerializer(many=True, read_only=True)

    class Meta:
        model = Entreprise
        fields = "__all__"

