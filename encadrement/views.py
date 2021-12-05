from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from encadrement.models import Reunion, Message
from encadrement.serializers import *


# Create your views here.       
@api_view(['GET','POST','PUT','DELETE'])
def reunion(request):
    if request.method == 'GET':
        getAll = Reunion.objects.all()
        serializer = ReunionSerializer(getAll, many=True)
        return Response(serializer.data)


@api_view(['GET','POST','PUT','DELETE'])
def message(request):
    if request.method == 'GET':
        getAll = Message.objects.all()
        serializer = MessageSerializer(getAll, many=True)
        return Response(serializer.data)

