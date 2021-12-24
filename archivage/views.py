from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from archivage.models import Rapport, Commentaires
from archivage.serializers import *


# Create your views here.       
@api_view(['GET','POST'])
def rapport(request):
    if request.method == 'GET':
        getAll = Rapport.objects.all()
        serializer = RapportSerializer(getAll, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        serializer = RapportSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getOneRapport(request, pk):
    try:
        data = Rapport.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RapportSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = RapportSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET','POST'])
def commentaires(request):
    if request.method == 'GET':
        getAll = Commentaires.objects.all()
        serializer = CommentairesSerializer(getAll, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        serializer = CommentairesSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


