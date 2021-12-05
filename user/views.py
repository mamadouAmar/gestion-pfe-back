from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user(request):
    if request.method == 'GET':
        getAll = User.objects.all()
        serializer = UserSerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def encadreur(request):
    if request.method == 'GET':
        getAll = Encadreur.objects.all()
        serializer = EncadreurSerializer(getAll, many=True)
        return Response(serializer.data)