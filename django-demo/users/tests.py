from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome, testuser')

    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_profile_edit(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('profile'), {
            'username': 'updateduser'
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(response.status_code, 302)  # Redirect after successful profile update