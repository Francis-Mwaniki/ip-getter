from django.urls import path
from .views import register,Login,custom_Logout,mainUser
from base.views import home
urlpatterns = [
    path("", home, name="home"),
     path("user/",mainUser, name="user"),
     path("logout/",custom_Logout , name="logout"),
    path("register/",register.as_view(),name='register'),
    path("login/", Login.as_view(),name='login')
    
]
