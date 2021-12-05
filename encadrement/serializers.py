from rest_framework import serializers
from encadrement.models import Message, Reunion


class ReunionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reunion
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"