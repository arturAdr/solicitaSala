from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from .serializers import AgendaSerializer
from .models import Agenda


class AgendaViewSet(viewsets.ModelViewSet):

    __basic_fields = ('inicio', 'titulo', 'fim', 'qtd_pessoas', 'sala')

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)

    filter_fields = __basic_fields
    search_fields = __basic_fields
