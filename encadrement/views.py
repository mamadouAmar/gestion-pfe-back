from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from encadrement.models import Reunion, Message
from encadrement.serializers import *


# Create your views here.       
@api_view(['GET','POST'])
def reunion(request):
    if request.method == 'GET':
        getAll = Reunion.objects.all()
        serializer = ReunionSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReunionSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getOneReunion(request, pk):
    try:
        data = Reunion.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReunionSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = ReunionSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)



@api_view(['GET','POST'])
def message(request):
    if request.method == 'GET':
        getAll = Message.objects.all()
        serializer = MessageSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getMessage(request, pfe):
    try:
        data = Message.objects.get(projet=pfe)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MessageSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = MessageSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)

