

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import UserRegistration

User = get_user_model()

class RegisterViewTests(TestCase):

    def setUp(self):
        self.url = reverse("account:register")

    def test_registration_success(self):
        """
        This test checks if a user can successfully register with valid 
        data and if they are redirected to the login page with a success 
        message.
        """
        
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password1': 'securepassword123',
            'password2': 'securepassword123'
        })

        # checks if the user is created
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(User.objects.get().username, 'testuser')

        # checks for redirection
        self.assertRedirects(response, reverse("login"))

    def test_get_registration_form(self):
        """
        Verify that a GET request to the registration page returns
          the registration form.
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], UserRegistration)

    def test_logged_in_user_redirect(self):
        """
        Test Redirect for Already Logged-In User.
        """

        self.client.login(username='testuser', password='securepassword123')

        response = self.client.get(self.url)
        #self.assertRedirects(response, reverse("cafetaria:home"))