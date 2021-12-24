from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from entreprise.models import Entreprise, Employe
from entreprise.serializers import *


# Create your views here.       
@api_view(['GET','POST'])
def entreprise(request):
    if request.method == 'GET':
        getAll = Entreprise.objects.all()
        serializer = EntrepriseSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EntrepriseSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def entreprise_(request, pk):
    try:
        data = Entreprise.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EntrepriseSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = EntrepriseSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET','POST'])
def employe(request):
    if request.method == 'GET':
        getAll = Employe.objects.all()
        serializer = EmployeSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employe_(request, pk):
    try:
        data = Employe.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EmployeSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = EmployeSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)
