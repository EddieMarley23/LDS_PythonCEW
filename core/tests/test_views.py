from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Car  # Certifique-se de que o caminho está correto
from django.core.files.uploadedfile import SimpleUploadedFile


class CarViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.car = Car.objects.create(model='Model S', brand='Tesla', plate='ABC1234', name='Test Car', createdby=self.user.id)

    def test_home_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.car.name)

    def test_home_view_unauthenticated(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_save_view(self):
        self.client.login(username='testuser', password='testpassword')
        file = SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(reverse('save'), {
            'model': 'Model X',
            'brand': 'Tesla',
            'plate': 'XYZ9876',
            'name': 'New Car',
            'createdby': self.user.id,
            'photo': file,
        })
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.assertTrue(Car.objects.filter(name='New Car').exists())

    def test_update_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('update', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')
        self.assertContains(response, self.car.name)

    def test_update_my_car_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('updateMyCar', args=[self.car.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'updateMyCar.html')
        self.assertContains(response, self.car.name)

    def test_updating_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('updating', args=[self.car.id]), {
            'model': 'Updated Model',
            'brand': 'Updated Brand',
            'plate': 'XYZ9876',
            'name': 'Updated Car',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.car.refresh_from_db()
        self.assertEqual(self.car.model, 'Updated Model')

    def test_to_assess_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('toAssess', args=[self.car.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.car.refresh_from_db()
        self.assertEqual(self.car.like, 1)

    def test_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete', args=[self.car.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'useremail': 'newuser@example.com',
            'password': 'newpassword',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to home

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect to login


