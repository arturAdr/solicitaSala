from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils.timezone import datetime
import base64
import datetime as dt
from model_mommy import mommy
from .models import Sala


class TestCriacaoSala(TestCase):

    def setUp(self):
        self.sala = mommy.make(Sala, titulo='Sala 01',
                               capacidade=5)

    def test_criar_sala(self):
        self.assertTrue(isinstance(self.sala, Sala))
        self.assertEquals(self.sala.__str__(), self.sala.titulo)


class SalaTestViewsPost(TestCase):

    def setUp(self):

        self.credentials = {
            'username': 'admin',
            'password': '123456789'}
        self.user = User.objects.create_user(**self.credentials)

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic {}'.format(base64.b64encode(b'admin:123456789').decode()),
        }

    def test_criacao_sala(self):

        data = {'titulo': 'Sala 03',
                'capacidade': 5}

        response = self.client.post('/salas/',  data, **self.auth_headers)

        self.assertTrue(response.status_code == 201)
        self.assertTrue(response.json()['titulo'] == data['titulo'])


class SalaTestViewsGet(TestCase):

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
                                 capacidade=2)

    def test_listagem_sala(self):

        response = self.client.get('/salas/',  **self.auth_headers)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()['count'] == 2)

    def test_listagem_com_filtro(self):

        response = self.client.get(
            '/salas/?titulo={}'.format(self.sala_2.titulo),  **self.auth_headers)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()['results']
                        [0]['titulo'] == self.sala_2.titulo)

    def test_com_ordenacao(self):

        response = self.client.get(
            '/salas/?ordering=capacidade',  **self.auth_headers)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()['results'][0]['capacidade'] < response.json()[
                        'results'][1]['capacidade'])

        response = self.client.get(
            '/salas/?ordering=-capacidade',  **self.auth_headers)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()['results'][0]['capacidade'] > response.json()[
                        'results'][1]['capacidade'])


class SalaTestViewsPut(TestCase):

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

    def test_atualizacao(self):

        response_get = self.client.get(
            '/salas/{}/'.format(self.sala_1.id),  **self.auth_headers)
        self.assertTrue(response_get.status_code == 200)
        self.assertTrue(response_get.json()[
                        'capacidade'] == self.sala_1.capacidade)
        self.assertTrue(response_get.json()['titulo'] == self.sala_1.titulo)

        data = {'titulo': 'Sala Alterada',
                'capacidade': 10}

        response_put = self.client.put('/salas/{}/'.format(self.sala_1.id),
                                       data, 'application/json', **self.auth_headers)
        self.assertTrue(response_put.status_code == 200)
        self.assertTrue(response_put.json()[
                        'capacidade'] == data['capacidade'])
        self.assertTrue(response_put.json()[
                        'titulo'] == data['titulo'])


class SalaTestViewsDelete(TestCase):

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

    def test_delete(self):

        response_get = self.client.get(
            '/salas/{}/'.format(self.sala_1.id),  **self.auth_headers)
        self.assertTrue(response_get.status_code == 200)

        response_delete = self.client.delete(
            '/salas/{}/'.format(self.sala_1.id),  **self.auth_headers)
        self.assertTrue(response_delete.status_code == 204)

        response_get = self.client.get(
            '/salas/{}/'.format(self.sala_1.id),  **self.auth_headers)
        self.assertTrue(response_get.status_code == 404)
