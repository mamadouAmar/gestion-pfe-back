from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from archivage.models import Rapport, Commentaires
from archivage.serializers import *


# Create your views here.       
@api_view(['GET','POST','PUT','DELETE'])
def rapport(request):
    if request.method == 'GET':
        getAll = Rapport.objects.all()
        serializer = RapportSerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET','POST','PUT','DELETE'])
def commentaires(request):
    if request.method == 'GET':
        getAll = Commentaires.objects.all()
        serializer = CommentairesSerializer(getAll, many=True)
        return Response(serializer.data)

