from django.urls import path
from . import views

app_name = "users"   


urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path("register", views.signup, name="register")
]