from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required


def is_cafe_admin(user):
    if user.is_authenticated and user.role == 'admin':
        return True
    if user.is_authenticated and user.role == 'customer':
        return False
    return False



@login_required
@user_passes_test(is_cafe_admin, login_url='cafetaria:handle_unauthorized_access')
def home_view(request):
    return render(request, 'cafeadmin/home.html')
