from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from entreprise.models import Entreprise, Employe
from entreprise.serializers import *


# Create your views here.       
@api_view(['GET','POST','PUT','DELETE'])
def entreprise(request):
    if request.method == 'GET':
        getAll = Entreprise.objects.all()
        serializer = EntrepriseSerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET','POST','PUT','DELETE'])
def employe(request):
    if request.method == 'GET':
        getAll = Employe.objects.all()
        serializer = EmployeSerializer(getAll, many=True)
        return Response(serializer.data)
