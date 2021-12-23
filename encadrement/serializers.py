from rest_framework import serializers
from encadrement.models import Message, Reunion
from etude.serializers import ProjetFinDetudesSerializer
from user.serializers import UserSerializer


class ReunionSerializer(serializers.ModelSerializer):

    projet = ProjetFinDetudesSerializer()
    participants = UserSerializer()
    
    class Meta:
        model = Reunion
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"