from django.urls import path

from soutenance.views import *


urlpatterns = [
    path('jury/', jury, name="jurys"),
    path('soutenance/', soutenance, name="soutenances"),
    path('appreciation/', appreciation, name="appreciations"),
    path('jury/<int:pk>/', jury_, name="jury"),
    path('soutenance/<int:pk>/', soutenance_, name="soutenance"),
    path('appreciation/<int:pk>/', appreciation_, name="appreciation")
]