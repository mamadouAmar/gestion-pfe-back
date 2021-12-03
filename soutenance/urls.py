from django.urls import path

from soutenance.views import appreciation, jury, soutenance


urlpatterns = [
    path('jury/', jury, name="jury"),
    path('soutenance/', soutenance, name="soutenance"),
    path('appreciation/', appreciation, name="appreciation"),
]