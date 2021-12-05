from rest_framework import serializers

from soutenance.models import Appreciations, Jury, Soutenance


class JurySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jury
        fields = "__all__"


class SoutenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soutenance
        fields = "__all__"


class AppreciationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appreciations
        fields = "__all__"