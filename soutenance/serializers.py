from os import read
from rest_framework import serializers
from etude.serializers import ProjetFinDetudesSerializer, SoutenantSerializer

from soutenance.models import Appreciations, Jury, Soutenance
from user.serializers import EncadreurSerializer


class JurySerializer(serializers.ModelSerializer):

    membres = EncadreurSerializer(many=True)

    class Meta:
        model = Jury
        fields = "__all__"


class SoutenanceSerializer(serializers.ModelSerializer):

    jury = JurySerializer()
    projet = ProjetFinDetudesSerializer(read_only=True)

    class Meta:
        model = Soutenance
        fields = "__all__"


class AppreciationsSerializer(serializers.ModelSerializer):

    soutenant = SoutenantSerializer()
    jury = JurySerializer()
    
    class Meta:
        model = Appreciations
        fields = "__all__"