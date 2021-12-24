from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def jury(request):
    if request.method == 'GET':
        getAll = Jury.objects.all()
        serializer = JurySerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JurySerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def jury_(request, pk):
    try:
        data = Jury.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = JurySerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = JurySerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def soutenance(request):
    if request.method == 'GET':
        getAll = Soutenance.objects.all()
        serializer = SoutenanceSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SoutenanceSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def soutenance_(request, pk):
    try:
        data = Soutenance.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SoutenanceSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = SoutenanceSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def appreciation(request):
    if request.method == 'GET':
        getAll = Appreciations.objects.all()
        serializer = AppreciationsSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AppreciationsSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def appreciation_(request, pk):
    try:
        data = Appreciations.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AppreciationsSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = AppreciationsSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)