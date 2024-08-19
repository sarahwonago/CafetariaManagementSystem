

from django.urls import path

from .views import register_view

app_name = "account"

urlpatterns = [
    path("user-registration/", register_view, name="register"),
    
]



# from .cbviews import UserRegistrationView, CustomLoginView

# urlpatterns = [
#     path('registration/', UserRegistrationView.as_view(), name='register'),
#     path("user-login/", CustomLoginView.as_view(), name="login"),
#     # other URL patterns
# ]