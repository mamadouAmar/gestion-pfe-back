from django.urls import path

from user.views import encadreur, user


urlpatterns = [
    path('user/', user, name="user"),
    path('encadreur/', encadreur, name="encadreur"),
]