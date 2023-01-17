from django.urls import path
from .views import register,Login
urlpatterns = [
    path("register/",register.as_view()),
    path("login/", Login.as_view())
]
