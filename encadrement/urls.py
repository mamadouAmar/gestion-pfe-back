from django.urls import path
from encadrement.views import reunion, message


urlpatterns = [
    path('reunion/', reunion, name="reunion"),
    path('message/', message, name="message"),
]