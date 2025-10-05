# wzertisAPI/tests/test_models.py
from django.test import TestCase
from django.core.exceptions import ValidationError
from wzertisAPI.models import Appeal, ArtGroup, Artwork

class AppealModelTest(TestCase):
    def test_valid_appeal(self):
        appeal = Appeal(
            name="Иван",
            email="ivan@example.com",
            theme="Вопрос",
            message="Как дела?"
        )
        appeal.full_clean()  # вызывает валидацию
        appeal.save()
        self.assertEqual(Appeal.objects.count(), 1)
        self.assertEqual(appeal.email, "ivan@example.com")

    def test_invalid_email(self):
        appeal = Appeal(
            name="Иван",
            email="not-an-email",
            theme="Тема",
            message="Сообщение"
        )
        with self.assertRaises(ValidationError):
            appeal.full_clean()

class ArtworkModelTest(TestCase):
    def test_artwork_str(self):
        group = ArtGroup.objects.create(title="Современное")
        artwork = Artwork.objects.create(
            title="Звёздная ночь",
            description="Описание",
            year=2023,
            group=group
        )
        self.assertEqual(str(artwork), "Звёздная ночь")