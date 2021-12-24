from django.urls import path
from encadrement.views import getMessage, getOneReunion, reunion, message


urlpatterns = [
    path('reunion/', reunion, name="reunions"),
    path('message/', message, name="messages"),
    path('message/<int:pfe>/', getMessage, name="message"),
    path('reunion/<int:pk>/', getOneReunion, name="reunion")
]