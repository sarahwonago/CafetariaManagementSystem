

from django.urls import path

from .views import home_view, handle_unauthorized_access

app_name="cafetaria"

urlpatterns=[
    path("", home_view, name="home"),
    path("unauthorized/", handle_unauthorized_access, name="handle_unauthorized_access"),
]