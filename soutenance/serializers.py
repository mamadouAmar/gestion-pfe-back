from rest_framework import serializers

from soutenance.models import Appreciations, Jury, Soutenance


class JurySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jury
        fields = all


class SoutenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soutenance
        fields = all


class AppreciationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appreciations
        fields = all