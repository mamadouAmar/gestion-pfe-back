from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def jury(request):
    if request.method == 'GET':
        getAll = Jury.objects.all()
        serializer = JurySerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def soutenance(request):
    if request.method == 'GET':
        getAll = Soutenance.objects.all()
        serializer = SoutenanceSerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def appreciation(request):
    if request.method == 'GET':
        getAll = Appreciations.objects.all()
        serializer = AppreciationsSerializer(getAll, many=True)
        return Response(serializer.data)