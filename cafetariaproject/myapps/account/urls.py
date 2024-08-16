

from django.urls import path

from .views import register_view

app_name = "account"

urlpatterns = [
    path("registration/", register_view, name="register"),
]



# from .cbviews import UserRegistrationView

# urlpatterns = [
#     path('registration/', UserRegistrationView.as_view(), name='register'),
#     # other URL patterns
# ]