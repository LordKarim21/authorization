from django.test import TestCase
from django.urls import reverse
from .models import Profile


class ProfileModelTests(TestCase):
    def test_profile_creation(self):
        profile = Profile.objects.create(phone_number='+1234567890')
        self.assertEqual(profile.phone_number, '+1234567890')


class AuthPhoneViewTests(TestCase):
    def test_auth_phone_view_get(self):
        response = self.client.get(reverse('auth_phone'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth_phone.html')

    def test_auth_phone_view_post(self):
        response = self.client.post(reverse('auth_phone'), {'phone_number': '+1234567890'})
        self.assertEqual(response.status_code, 302)  # Redirect to auth_code view


class AuthCodeViewTests(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(phone_number='+1234567890', code='1234')

    def test_auth_code_view_get(self):
        response = self.client.get(reverse('auth_code', args=['+1234567890']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth_code.html')

    def test_auth_code_view_post_correct_code(self):
        response = self.client.post(reverse('auth_code', args=['+1234567890']), {'code': '1234'})
        self.assertEqual(response.status_code, 302)  # Redirect to profile view

    def test_auth_code_view_post_incorrect_code(self):
        response = self.client.post(reverse('auth_code', args=['+1234567890']), {'code': '5678'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid code. Please try again.')


class ProfileViewTests(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(phone_number='+1234567890')

    def test_profile_view_get(self):
        response = self.client.get(reverse('profile', args=['+1234567890']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_profile_view_post(self):
        response = self.client.post(reverse('profile', args=['+1234567890']), {'invite_code': 'ABC123'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.profile.invite_code, 'ABC123')
        self.assertTrue(self.profile.activated_invite_code)
