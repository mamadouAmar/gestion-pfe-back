from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def departement(request):
    if request.method == 'GET':
        getAll = Departement.objects.all()
        serializer = DepartementSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepartementSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def departement_(request, pk):
    try:
        data = Departement.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DepartementSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = DepartementSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def professeur(request):
    if request.method == 'GET':
        getAll = Professeur.objects.all()
        serializer = ProfesseurSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfesseurSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def professeur_(request, pk):
    try:
        data = Professeur.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfesseurSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = ProfesseurSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def competence(request):
    if request.method == 'GET':
        getAll = Competence.objects.all()
        serializer = CompetenceSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompetenceSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def competence_(request, pk):
    try:
        data = Competence.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CompetenceSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = CompetenceSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def projetFinDetudes(request):
    if request.method == 'GET':
        getAll = ProjetFinDetudes.objects.all()
        serializer = ProjetFinDetudesSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompetenceSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def projetFinDetudes_(request, pk):
    try:
        data = ProjetFinDetudes.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProjetFinDetudesSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = ProjetFinDetudesSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST'])
def etudiant(request):
    if request.method == 'GET':
        getAll = Etudiant.objects.all()
        serializer = EtudiantSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompetenceSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def etudiant_(request, pk):
    try:
        data = Etudiant.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EtudiantSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = EtudiantSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def soutenant(request):
    if request.method == 'GET':
        getAll = Soutenant.objects.all()
        serializer = SoutenantSerializer(getAll, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompetenceSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def soutenant_(request, pk):
    try:
        data = Soutenant.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SoutenantSerializer(data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        serializer = SoutenantSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(data, status=status.HTTP_202_ACCEPTED)