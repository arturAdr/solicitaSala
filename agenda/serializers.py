from rest_framework import serializers

from .models import Agenda


class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agenda
        fields = ('url', 'titulo', 'inicio', 'fim', 'qtd_pessoas', 'sala')

    def validate(self, data):

        if data['qtd_pessoas'] > data['sala'].capacidade:
            raise serializers.ValidationError(
                "Capacidade nao suportada pela sala")

        if data['inicio'] > data['fim']:
            raise serializers.ValidationError(
                "Data final invalida, por favor informe uma data final maior que a data inicio")

        agendas = data['sala'].agenda_set.all()
        for a in agendas:
            if (data['inicio'] >= a.inicio
                and data['inicio'] <= a.fim
                or data['inicio'] <= a.inicio and
                    data['fim'] >= a.inicio):
                raise serializers.ValidationError(
                    "Sala indisponivel para reserva")

        return data
