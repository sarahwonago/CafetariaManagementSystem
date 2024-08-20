

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

#  defines a role based  redirect function for customers
def is_customer(user):
    if user.is_authenticated and user.role == 'customer':
        return True
    if user.is_authenticated and user.role == 'admin':
        return False
    return False

# Custom view to handle unauthorized access for both roles
def handle_unauthorized_access(request):

    """
    Redirect logged-in users to their respective homepages if they are
    already authenticated but trying to access an unauthorized view.
    """
    
    user = request.user
    if user.role == 'customer':
        return redirect('cafetaria:home')
    elif user.role == 'admin':
        return redirect('cafeadmin:home')
    else:
        return redirect('login')
    
@login_required
@user_passes_test(is_customer, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def home_view(request):

    """
    Renders the home page for authenticated users.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """


    return render(request, "cafetaria/home.html")
