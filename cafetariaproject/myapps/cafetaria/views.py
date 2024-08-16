

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home_view(request):

    """
    Renders the home page for authenticated users.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """


    return render(request, "cafetaria/home.html")
