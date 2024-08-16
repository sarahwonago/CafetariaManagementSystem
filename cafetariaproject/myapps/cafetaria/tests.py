from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

from .views import home_view

User = get_user_model()


class HomeViewTests(TestCase):
    """
    Tests for the home_view.
    """

    def setUp(self):
        """
        Create a user for authenticated tests.
        """
        self.user = User.objects.create_user(
            username="username",
            password="securepassword123"

        )
        self.login_url = reverse("login")
        self.home_url = reverse("cafetaria:home")

    def test_home_view_accessible_by_authenticated_user(self):
        """
        Test that the home view is accessible to authenticated users.
        """
        self.client.login(username='username', password='securepassword123')
        response = self.client.get(self.home_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cafetaria/home.html')

        #tests that home url name resolves to home view function
        self.assertTrue(resolve(self.home_url).func, home_view)

    def test_home_view_redirects_unauthenticated_user(self):
        """
        Test that the home view redirects unauthenticated users to the login page.
        """
        response = self.client.get(self.home_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.home_url}')


