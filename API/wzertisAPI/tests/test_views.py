# wzertisAPI/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from wzertisAPI.models import Appeal, ArtGroup, Artwork

class AppealAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_appeal_success(self):
        url = reverse('appeal')
        data = {
            'name': 'Петр',
            'email': 'petr@example.com',
            'theme': 'Предложение',
            'message': 'Добавьте темную тему!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Appeal.objects.count(), 1)
        self.assertEqual(response.data['name'], 'Петр')

    def test_create_appeal_invalid(self):
        url = reverse('appeal')
        data = {'name': 'Петр'}  # недостаточно данных
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Appeal.objects.count(), 0)

class ArtworkAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.group = ArtGroup.objects.create(title="Современное искусство")

    def test_groups_list(self):
        url = reverse('groups')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Современное искусство")

    def test_artworks_list(self):
        Artwork.objects.create(
            title="Работа 1", description="...", year=2020, group=self.group
        )
        url = reverse('artworks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_fav_works(self):
        Artwork.objects.create(
            title="Избранная работа",
            description="Описание",
            year=2023,
            group=self.group,
            favorite=True
        )
        url = reverse('fav_works')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Избранная работа")

    def test_get_group_by_id(self):
        url = reverse('group_id', args=[self.group.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.group.title)

    def test_get_group_by_id_not_found(self):
        url = reverse('group_id', args=[999])
        response = self.client.get(url)
        # В текущей реализации view упадёт с 500, но мы ожидаем 404
        # → рекомендуется исправить view (см. ниже)
        # self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

        # После исправления view (см. примечание) будет:
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)