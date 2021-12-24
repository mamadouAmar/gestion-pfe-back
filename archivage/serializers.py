from rest_framework import serializers

from archivage.models import Commentaires, Rapport

class CommentairesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaires
        fields = "__all__"


class RapportSerializer(serializers.ModelSerializer):

    commentaires = CommentairesSerializer(many=True, read_only=True)

    class Meta:
        model = Rapport
        fields = "__all__"