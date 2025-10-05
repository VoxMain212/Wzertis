# wzertisAPI/tests/test_serializers.py
from django.test import TestCase
from wzertisAPI.serializers import AppealSerializer, ArtworkSerializer
from wzertisAPI.models import ArtGroup, Artwork

class AppealSerializerTest(TestCase):
    def test_valid_data(self):
        data = {
            'name': 'Анна',
            'email': 'anna@test.com',
            'theme': 'Обратная связь',
            'message': 'Отличный сайт!'
        }
        serializer = AppealSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['email'], 'anna@test.com')

    def test_invalid_email(self):
        data = {'name': 'Анна', 'email': 'invalid-email', 'theme': 'Тема', 'message': 'Сообщение'}
        serializer = AppealSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_missing_required_field(self):
        data = {'name': 'Анна', 'theme': 'Тема'}
        serializer = AppealSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
        self.assertIn('message', serializer.errors)

class ArtworkSerializerTest(TestCase):
    def test_includes_image_url(self):
        group = ArtGroup.objects.create(title="Тест")
        artwork = Artwork.objects.create(
            title="Работа",
            description="Описание",
            year=2020,
            group=group
        )
        serializer = ArtworkSerializer(artwork)
        self.assertIn('image', serializer.data)