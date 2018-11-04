from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils.timezone import datetime
import base64
import datetime as dt
from model_mommy import mommy
from .models import Agenda
from sala.models import Sala


class TestCriacaoAgenda(TestCase):

    def setUp(self):
        self.sala = mommy.make(Sala, titulo='Sala 01',
                               capacidade=5)
        self.agenda = mommy.make(Agenda, titulo="agenda test", inicio=dt.datetime.now(),
                                 fim=dt.datetime.now(), qtd_pessoas=5, sala=self.sala)

    def test_criacao_agenda(self):
        self.assertTrue(isinstance(self.agenda, Agenda))
        self.assertEquals(self.agenda.__str__(),
                          '{}-{}-{}-{}'.format(self.agenda.titulo, self.agenda.inicio,
                                               self.agenda.fim, self.sala.titulo))


class AgendaTestViewsPost(TestCase):

    def setUp(self):

        self.credentials = {
            'username': 'admin',
            'password': '123456789'}
        self.user = User.objects.create_user(**self.credentials)

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic {}'.format(base64.b64encode(b'admin:123456789').decode()),
        }

        self.sala = mommy.make(Sala, titulo='Sala 01',
                               capacidade=5)

        self.agenda = mommy.make(Agenda, titulo="agenda test", inicio=dt.datetime(2018, 11, 4, 16, 00),
                                 fim=dt.datetime(2018, 11, 4, 21, 00), qtd_pessoas=5, sala=self.sala)

    def test_criacao(self):

        data = {
            'titulo': 'agenda test',
            'inicio': '2018-01-01T00:00:00Z',
            'fim': '2018-01-01T01:00:00Z',
            'qtd_pessoas': 5,
            'sala': self.sala.pk}

        response = self.client.post('/agendas/',  data, **self.auth_headers)

        self.assertTrue(response.status_code == 201)
        self.assertTrue(response.json()['inicio'] == data['inicio'])

    def test_criacao_indinsponivel(self):

        data = {
            'titulo': 'agenda test',
            'inicio': '2018-11-04T01:00:00Z',
            'fim': '2018-01-01T023:00:00Z',
            'qtd_pessoas': 500,
            'sala': self.sala.pk}

        response_sala_indisponivel = self.client.post(
            '/agendas/',  data, **self.auth_headers)
        self.assertTrue(response_sala_indisponivel.status_code == 400)


class AgendaTestViewsGet(TestCase):

    def setUp(self):

        self.credentials = {
            'username': 'admin',
            'password': '123456789'}
        self.user = User.objects.create_user(**self.credentials)

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic {}'.format(base64.b64encode(b'admin:123456789').decode()),
        }

        self.sala_1 = mommy.make(Sala, titulo='Sala 01',
                                 capacidade=5)

        self.sala_2 = mommy.make(Sala, titulo='Sala 02',
                                 capacidade=10)

        self.agenda_1 = mommy.make(Agenda, titulo="agenda test", inicio=dt.datetime.now(),
                                   fim=dt.datetime.now() + dt.timedelta(hours=3), qtd_pessoas=5, sala=self.sala_1)

        self.agenda_2 = mommy.make(Agenda, titulo="agenda test", inicio=dt.datetime.now(),
                                   fim=dt.datetime.now(), qtd_pessoas=7, sala=self.sala_2)

    def test_listagem(self):

        response = self.client.get('/agendas/',  **self.auth_headers)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()['count'] == 2)

    def test_listagem_com_filtro(self):

        response = self.client.get(
            '/agendas/?qtd_pessoas={}'.format(self.agenda_2.qtd_pessoas),  **self.auth_headers)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()['results'][0]
                        ['qtd_pessoas'] == self.agenda_2.qtd_pessoas)

    def test_listagem_comordenacao(self):

        response = self.client.get(
            '/agendas/?ordering=qtd_pessoas',  **self.auth_headers)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()['results'][0]['qtd_pessoas'] < response.json()[
                        'results'][1]['qtd_pessoas'])

        response = self.client.get(
            '/agendas/?ordering=-qtd_pessoas',  **self.auth_headers)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()['results'][0]['qtd_pessoas'] > response.json()[
                        'results'][1]['qtd_pessoas'])


class AgendaTestViewsPut(TestCase):

    def setUp(self):

        self.credentials = {
            'username': 'admin',
            'password': '123456789'}
        self.user = User.objects.create_user(**self.credentials)

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic {}'.format(base64.b64encode(b'admin:123456789').decode()),
        }

        self.sala_1 = mommy.make(Sala, titulo='Sala 01',
                                 capacidade=5)

        self.sala_2 = mommy.make(Sala, titulo='Sala 02',
                                 capacidade=10)

        self.agenda_1 = mommy.make(Agenda, titulo="agenda test", inicio=dt.datetime.now(),
                                   fim=dt.datetime.now(), qtd_pessoas=7, sala=self.sala_2)

    def test_atualizacao(self):
        response_get = self.client.get(
            '/agendas/{}/'.format(self.agenda_1.id),  **self.auth_headers)
        self.assertTrue(response_get.status_code == 200)
        self.assertTrue(response_get.json()[
                        'qtd_pessoas'] == self.agenda_1.qtd_pessoas)

        data = {'titulo': 'agenda test',
                'inicio': '2019-01-01T00:00:00Z',
                'fim': '2019-01-01T02:00:00Z', 'qtd_pessoas': 3, 'sala': self.sala_1.pk}

        response_put = self.client.put('/agendas/{}/'.format(self.agenda_1.id),
                                       data, 'application/json', **self.auth_headers)
        self.assertTrue(response_put.status_code == 200)
        self.assertTrue(response_put.json()[
                        'qtd_pessoas'] == data['qtd_pessoas'])


class AgendaTestViewsDelete(TestCase):

    def setUp(self):

        self.credentials = {
            'username': 'admin',
            'password': '123456789'}
        self.user = User.objects.create_user(**self.credentials)

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic {}'.format(base64.b64encode(b'admin:123456789').decode()),
        }

        self.sala_1 = mommy.make(Sala, titulo='Sala 01',
                                 capacidade=5)

        self.sala_2 = mommy.make(Sala, titulo='Sala 02',
                                 capacidade=10)

        self.agenda_1 = mommy.make(Agenda, titulo="agenda test", inicio=dt.datetime.now(),
                                   fim=dt.datetime.now() + dt.timedelta(hours=3), qtd_pessoas=5, sala=self.sala_1)

    def test_delete(self):

        response_get = self.client.get(
            '/agendas/{}/'.format(self.agenda_1.id),  **self.auth_headers)
        self.assertTrue(response_get.status_code == 200)

        response_delete = self.client.delete(
            '/agendas/{}/'.format(self.agenda_1.id),  **self.auth_headers)
        self.assertTrue(response_delete.status_code == 204)

        response_get = self.client.get(
            '/agendas/{}/'.format(self.agenda_1.id),  **self.auth_headers)
        self.assertTrue(response_get.status_code == 404)
