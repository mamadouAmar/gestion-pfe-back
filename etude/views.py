from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def departement(request):
    if request.method == 'GET':
        getAll = Departement.objects.all()
        serializer = DepartementSerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def professeur(request):
    if request.method == 'GET':
        getAll = Professeur.objects.all()
        serializer = ProfesseurSerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def competence(request):
    if request.method == 'GET':
        getAll = Competence.objects.all()
        serializer = CompetenceSerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def projetFinDetudes(request):
    if request.method == 'GET':
        getAll = ProjetFinDetudes.objects.all()
        serializer = ProjetFinDetudesSerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def etudiant(request):
    if request.method == 'GET':
        getAll = Etudiant.objects.all()
        serializer = EtudiantSerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def soutenant(request):
    if request.method == 'GET':
        getAll = Soutenant.objects.all()
        serializer = SoutenantSerializer(getAll, many=True)
        return Response(serializer.data)