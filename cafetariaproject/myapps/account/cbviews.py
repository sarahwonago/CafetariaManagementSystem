from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import UserRegistration

User = get_user_model()

class UserRegistrationView(CreateView):
    form_class = UserRegistration
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """
        Handles successful form submissions.
        """
        response = super().form_valid(form)
        messages.success(self.request, "Registration successful! Please log in.")
        return response
    
    def form_invalid(self, form):
        """
        Handles form errors.
        """
        messages.error(self.request, "There was an error with your registration. Please correct the errors below.")
        return super().form_invalid(form)
    
    def get(self, request, *args, **kwargs):

        """
        Redirects authenticated users.
        """

        if request.user.is_authenticated:
            return redirect(reverse_lazy("cafetaria:home"))
        
        return super().get(request, *args, **kwargs)
    

    class CustomLoginView(LoginView):
        """
        Custom Login View to handle different user roles.
        """

        def get_success_url(self):

            user = self.request.user

            if user.role == 'admin':
                return reverse_lazy('cafeadmin:home')
            elif user.role == 'customer':
                return reverse_lazy('cafetaria:home')
            
            return super().get_success_url()