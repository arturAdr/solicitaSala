from rest_framework import serializers

from .models import Agenda


class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agenda
        fields = ('url', 'data_inicio', 'data_final', 'qtd_pessoas', 'sala')

    def validate(self, data):

        if data['qtd_pessoas'] > data['sala'].capacidade:
            raise serializers.ValidationError(
                "Capacidade nao suportada pela sala")

        if data['data_inicio'] > data['data_final']:
            raise serializers.ValidationError(
                "Data final invalida, por favor informe uma data final maior que a data inicio")

        agendas = data['sala'].agenda_set.all()
        for a in agendas:
            if (data['data_inicio'] > a.data_inicio
                and data['data_inicio'] < a.data_final
                or data['data_inicio'] < a.data_inicio and
                    data['data_final'] > a.data_inicio):
                raise serializers.ValidationError(
                    "Sala indisponivel para reserva")

        return data
