from rest_framework import serializers

from archivage.models import Commentaires, Rapport


class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = "__all__"


class CommentairesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaires
        fields = "__all__"