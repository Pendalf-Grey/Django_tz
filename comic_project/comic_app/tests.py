from django.test import TestCase
from .models import User, Comic, Rating


class UserTestCase(TestCase):
    def test_create_user(self):
        inicial_user_count = User.objects.count()
        new_user_data = (
            'username'
            'testuser'
            'password'
            'email'
            'test@example.com'
        )
        response = self.client.post('/create_user/', new_user_data)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(inicial_user_count.email, 'test@example.com')


class RatingTestCase(TestCase):
    def test_average_rating(self):
        product = Comic.objects.create(name='Test Product')  # создаём комикс для тестов

        Rating.objects.create(product=product, rating=4)  # создаём новую оценку
        Rating.objects.create(product=product, rating=5)

        average_rating = product.calculate_average_rating()  # вычисляем среднюю оценку

        self.assertEqual(average_rating, 4.5)  # проверяем, что оценка комикса равна 4.5

        average_rating.save()