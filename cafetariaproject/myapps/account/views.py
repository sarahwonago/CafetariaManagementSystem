from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView

from .forms import UserRegistration


def register_view(request):
    """
    View to handle user registration.
    """

    # Redirects authenticated users to home page
    if request.user.is_authenticated:
        return redirect(reverse_lazy("cafetaria:home"))
    
    # Handle form submission
    if request.method == 'POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful, please Login")
            return redirect(reverse_lazy("login"))

    else:
        form=UserRegistration()

    # pass the form to the template context
    context ={
        "form":form,
    }
    
    return render(request,"registration/register.html", context)

# class CustomLoginView(LoginView):
#     """
#     Custom Login View to handle different user roles.
#     """

#     def get_success_url(self):

#         user = self.request.user

#         if user.role == 'admin':
#             return reverse_lazy('cafeadmin:home')
#         elif user.role == 'customer':
#             return reverse_lazy('cafetaria:home')
        
#         return super().get_success_url()

