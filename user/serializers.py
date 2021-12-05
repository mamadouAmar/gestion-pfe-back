from rest_framework import serializers

from user.models import Encadreur, User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class EncadreurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Encadreur
        fields = "__all__"